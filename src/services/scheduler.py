"""
Task scheduler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from src.database.database import get_db_session, Order, User
from src.services.automation.social_media_bot import SocialMediaBot
from src.utils.logger import setup_logger, log_system_event

logger = setup_logger()

class TaskScheduler:
    """Task scheduler for managing automation tasks"""
    
    def __init__(self):
        self.running = False
        self.tasks: Dict[str, asyncio.Task] = {}
        self.social_bot = SocialMediaBot()
        
    async def start(self):
        """Start the task scheduler"""
        if self.running:
            return
        
        self.running = True
        logger.info("Task scheduler starting...")
        
        # Start background tasks
        self.tasks['order_processor'] = asyncio.create_task(self.process_orders())
        self.tasks['system_maintenance'] = asyncio.create_task(self.system_maintenance())
        self.tasks['user_cleanup'] = asyncio.create_task(self.user_cleanup())
        
        log_system_event("scheduler_start", "Task scheduler started successfully")
        
    async def stop(self):
        """Stop the task scheduler"""
        if not self.running:
            return
        
        self.running = False
        logger.info("Task scheduler stopping...")
        
        # Cancel all tasks
        for task_name, task in self.tasks.items():
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    logger.info(f"Task {task_name} cancelled")
        
        self.tasks.clear()
        log_system_event("scheduler_stop", "Task scheduler stopped")
        
    async def process_orders(self):
        """Process pending orders continuously"""
        while self.running:
            try:
                await self._process_pending_orders()
                await asyncio.sleep(30)  # Check every 30 seconds
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in order processor: {e}")
                await asyncio.sleep(60)  # Wait longer on error
    
    async def _process_pending_orders(self):
        """Process all pending orders"""
        try:
            from sqlalchemy import select
            
            async with get_db_session() as session:
                # Get pending orders
                result = await session.execute(
                    select(Order).where(Order.status == 'pending')
                    .order_by(Order.created_at)
                    .limit(10)  # Process 10 orders at a time
                )
                pending_orders = result.scalars().all()
                
                for order in pending_orders:
                    try:
                        await self._process_single_order(order, session)
                    except Exception as e:
                        logger.error(f"Error processing order {order.id}: {e}")
                        # Mark order as failed
                        order.status = 'failed'
                        order.error_message = str(e)
                        await session.commit()
                
        except Exception as e:
            logger.error(f"Error in _process_pending_orders: {e}")
    
    async def _process_single_order(self, order: Order, session):
        """Process a single order"""
        try:
            logger.info(f"Processing order {order.id} - {order.service_type}")
            
            # Update order status to processing
            order.status = 'processing'
            order.started_at = datetime.utcnow()
            await session.commit()
            
            # Process based on service type
            success = await self.social_bot.process_order(order)
            
            if success:
                order.status = 'completed'
                order.completed_at = datetime.utcnow()
                order.completed_quantity = order.quantity
                order.progress_percentage = 100.0
                
                logger.info(f"Order {order.id} completed successfully")
                log_system_event("order_completed", f"Order {order.id} completed", logging.INFO)
            else:
                order.status = 'failed'
                order.error_message = "Processing failed"
                
                # Refund tokens to user
                await self._refund_order_tokens(order, session)
                
                logger.warning(f"Order {order.id} failed")
                log_system_event("order_failed", f"Order {order.id} failed", logging.WARNING)
            
            await session.commit()
            
        except Exception as e:
            logger.error(f"Error processing order {order.id}: {e}")
            raise
    
    async def _refund_order_tokens(self, order: Order, session):
        """Refund tokens for failed order"""
        try:
            from src.database.database import update_user_tokens
            
            await update_user_tokens(
                user_id=order.user_id,
                amount=order.tokens_cost,
                transaction_type="refund",
                source="order_refund",
                description=f"Refund untuk pesanan #{order.id} yang gagal",
                reference_id=str(order.id)
            )
            
            logger.info(f"Refunded {order.tokens_cost} tokens for order {order.id}")
            
        except Exception as e:
            logger.error(f"Error refunding tokens for order {order.id}: {e}")
    
    async def system_maintenance(self):
        """Perform system maintenance tasks"""
        while self.running:
            try:
                await self._cleanup_old_logs()
                await self._update_user_statistics()
                await self._check_system_health()
                
                # Run maintenance every hour
                await asyncio.sleep(3600)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in system maintenance: {e}")
                await asyncio.sleep(1800)  # Wait 30 minutes on error
    
    async def _cleanup_old_logs(self):
        """Clean up old log files"""
        try:
            import os
            import glob
            from datetime import datetime, timedelta
            
            logs_dir = "logs"
            if not os.path.exists(logs_dir):
                return
            
            # Delete logs older than 30 days
            cutoff_date = datetime.now() - timedelta(days=30)
            
            for log_file in glob.glob(f"{logs_dir}/*.log*"):
                try:
                    file_time = datetime.fromtimestamp(os.path.getmtime(log_file))
                    if file_time < cutoff_date:
                        os.remove(log_file)
                        logger.info(f"Deleted old log file: {log_file}")
                except Exception as e:
                    logger.error(f"Error deleting log file {log_file}: {e}")
            
        except Exception as e:
            logger.error(f"Error in log cleanup: {e}")
    
    async def _update_user_statistics(self):
        """Update user statistics"""
        try:
            from sqlalchemy import select, func
            
            async with get_db_session() as session:
                # Update last active for users who haven't been active recently
                cutoff_time = datetime.utcnow() - timedelta(hours=24)
                
                result = await session.execute(
                    select(User).where(User.last_active < cutoff_time)
                )
                inactive_users = result.scalars().all()
                
                logger.info(f"Found {len(inactive_users)} inactive users")
                
        except Exception as e:
            logger.error(f"Error updating user statistics: {e}")
    
    async def _check_system_health(self):
        """Check system health and performance"""
        try:
            import psutil
            
            # Check memory usage
            memory = psutil.virtual_memory()
            if memory.percent > 90:
                log_system_event("high_memory_usage", f"Memory usage: {memory.percent}%", logging.WARNING)
            
            # Check disk usage
            disk = psutil.disk_usage('/')
            if disk.percent > 90:
                log_system_event("high_disk_usage", f"Disk usage: {disk.percent}%", logging.WARNING)
            
            # Check database connection
            async with get_db_session() as session:
                await session.execute(select(1))
            
            log_system_event("health_check", "System health check completed", logging.INFO)
            
        except Exception as e:
            logger.error(f"Error in system health check: {e}")
            log_system_event("health_check_failed", f"Health check failed: {e}", logging.ERROR)
    
    async def user_cleanup(self):
        """Clean up inactive users and data"""
        while self.running:
            try:
                await self._cleanup_inactive_users()
                await self._cleanup_old_orders()
                
                # Run cleanup daily
                await asyncio.sleep(86400)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in user cleanup: {e}")
                await asyncio.sleep(3600)  # Wait 1 hour on error
    
    async def _cleanup_inactive_users(self):
        """Clean up users who haven't been active for a long time"""
        try:
            from sqlalchemy import select
            
            # Users inactive for more than 90 days
            cutoff_date = datetime.utcnow() - timedelta(days=90)
            
            async with get_db_session() as session:
                result = await session.execute(
                    select(User).where(
                        User.last_active < cutoff_date,
                        User.tokens == 0,
                        User.is_premium == False
                    )
                )
                inactive_users = result.scalars().all()
                
                logger.info(f"Found {len(inactive_users)} users for cleanup consideration")
                
                # For now, just log. In production, you might want to:
                # - Send reactivation messages
                # - Archive user data
                # - Delete completely inactive accounts
                
        except Exception as e:
            logger.error(f"Error in inactive user cleanup: {e}")
    
    async def _cleanup_old_orders(self):
        """Clean up old completed orders"""
        try:
            from sqlalchemy import select, delete
            
            # Orders older than 6 months
            cutoff_date = datetime.utcnow() - timedelta(days=180)
            
            async with get_db_session() as session:
                # Count old orders
                result = await session.execute(
                    select(func.count(Order.id)).where(
                        Order.created_at < cutoff_date,
                        Order.status.in_(['completed', 'failed', 'cancelled'])
                    )
                )
                old_orders_count = result.scalar() or 0
                
                if old_orders_count > 0:
                    logger.info(f"Found {old_orders_count} old orders for potential cleanup")
                    
                    # For now, just log. In production, you might want to:
                    # - Archive old orders to separate table
                    # - Keep only summary statistics
                    # - Delete very old orders
                
        except Exception as e:
            logger.error(f"Error in old orders cleanup: {e}")
    
    async def add_priority_order(self, order_id: int):
        """Add a priority order for immediate processing"""
        try:
            from sqlalchemy import select
            
            async with get_db_session() as session:
                result = await session.execute(
                    select(Order).where(Order.id == order_id)
                )
                order = result.scalar_one_or_none()
                
                if order and order.status == 'pending':
                    # Process immediately
                    await self._process_single_order(order, session)
                    logger.info(f"Priority order {order_id} processed")
                
        except Exception as e:
            logger.error(f"Error processing priority order {order_id}: {e}")
    
    def get_status(self) -> Dict:
        """Get scheduler status"""
        return {
            'running': self.running,
            'active_tasks': len([t for t in self.tasks.values() if not t.done()]),
            'total_tasks': len(self.tasks),
            'uptime': datetime.utcnow().isoformat() if self.running else None
        }
