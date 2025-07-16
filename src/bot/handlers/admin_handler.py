"""
Admin command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id, get_db_session, User, Order, TokenTransaction
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_admin_keyboard, get_main_menu_keyboard

logger = setup_logger()

async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /admin command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "admin_command", "")
        
        # Check if user is admin
        admin_ids = os.getenv('ADMIN_USER_IDS', '').split(',')
        
        if str(user.id) not in admin_ids:
            await update.message.reply_text(
                "❌ **Akses Ditolak**\n\n"
                "Anda tidak memiliki akses ke panel admin.",
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Get admin statistics
        stats = await get_admin_statistics()
        
        # Admin panel message
        admin_text = f"""
🔧 **Admin Panel - Jam Tayang Pro**

📊 **Statistik Sistem:**

👥 **Users:**
• Total Users: {stats['total_users']:,}
• Active Today: {stats['active_today']:,}
• New Today: {stats['new_today']:,}
• Premium Users: {stats['premium_users']:,}
• Banned Users: {stats['banned_users']:,}

📋 **Orders:**
• Total Orders: {stats['total_orders']:,}
• Pending: {stats['pending_orders']:,}
• Processing: {stats['processing_orders']:,}
• Completed: {stats['completed_orders']:,}
• Failed: {stats['failed_orders']:,}
• Today's Orders: {stats['orders_today']:,}

💰 **Tokens:**
• Total Distributed: {stats['total_tokens_distributed']:,}
• Spent Today: {stats['tokens_spent_today']:,}
• Earned Today: {stats['tokens_earned_today']:,}
• Average per User: {stats['avg_tokens_per_user']:.1f}

📺 **Advertisements:**
• Views Today: {stats['ad_views_today']:,}
• Total Views: {stats['total_ad_views']:,}
• Tokens from Ads: {stats['tokens_from_ads']:,}

🖥️ **System Info:**
• Uptime: {stats['uptime']}
• Memory Usage: {stats['memory_usage']}
• Active Tasks: {stats['active_tasks']:,}
• Database Size: {stats['db_size']}

📈 **Performance:**
• Success Rate: {stats['success_rate']:.1f}%
• Avg Processing Time: {stats['avg_processing_time']}
• Error Rate: {stats['error_rate']:.2f}%

Gunakan menu di bawah untuk mengelola sistem.

---
*Admin Panel - Kantong Aplikasi 2025*
        """
        
        await update.message.reply_text(
            admin_text,
            parse_mode='Markdown',
            reply_markup=get_admin_keyboard()
        )
        
        logger.info(f"Admin panel accessed by user {user.id}")
        
    except Exception as e:
        logger.error(f"Error in admin_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat mengakses panel admin.",
            reply_markup=get_main_menu_keyboard()
        )

async def get_admin_statistics():
    """Get comprehensive admin statistics"""
    try:
        from sqlalchemy import select, func, and_
        from datetime import datetime, timedelta
        import psutil
        
        stats = {}
        today = datetime.utcnow().date()
        
        async with get_db_session() as session:
            # User statistics
            result = await session.execute(select(func.count(User.id)))
            stats['total_users'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(User.id)).where(
                    func.date(User.last_active) == today
                )
            )
            stats['active_today'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(User.id)).where(
                    func.date(User.registration_date) == today
                )
            )
            stats['new_today'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(User.id)).where(User.is_premium == True)
            )
            stats['premium_users'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(User.id)).where(User.is_banned == True)
            )
            stats['banned_users'] = result.scalar() or 0
            
            # Order statistics
            result = await session.execute(select(func.count(Order.id)))
            stats['total_orders'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(Order.id)).where(Order.status == 'pending')
            )
            stats['pending_orders'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(Order.id)).where(Order.status == 'processing')
            )
            stats['processing_orders'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(Order.id)).where(Order.status == 'completed')
            )
            stats['completed_orders'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(Order.id)).where(Order.status == 'failed')
            )
            stats['failed_orders'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.count(Order.id)).where(
                    func.date(Order.created_at) == today
                )
            )
            stats['orders_today'] = result.scalar() or 0
            
            # Token statistics
            result = await session.execute(
                select(func.sum(User.total_earned_tokens))
            )
            stats['total_tokens_distributed'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.sum(TokenTransaction.amount)).where(
                    and_(
                        func.date(TokenTransaction.created_at) == today,
                        TokenTransaction.amount < 0
                    )
                )
            )
            stats['tokens_spent_today'] = abs(result.scalar() or 0)
            
            result = await session.execute(
                select(func.sum(TokenTransaction.amount)).where(
                    and_(
                        func.date(TokenTransaction.created_at) == today,
                        TokenTransaction.amount > 0
                    )
                )
            )
            stats['tokens_earned_today'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.avg(User.tokens))
            )
            stats['avg_tokens_per_user'] = result.scalar() or 0
            
            # Ad statistics
            from src.database.database import AdView
            result = await session.execute(
                select(func.count(AdView.id)).where(
                    func.date(AdView.started_at) == today
                )
            )
            stats['ad_views_today'] = result.scalar() or 0
            
            result = await session.execute(select(func.count(AdView.id)))
            stats['total_ad_views'] = result.scalar() or 0
            
            result = await session.execute(
                select(func.sum(TokenTransaction.amount)).where(
                    TokenTransaction.source == 'ad_view'
                )
            )
            stats['tokens_from_ads'] = result.scalar() or 0
        
        # System statistics
        try:
            # Uptime (mock - implement actual uptime tracking)
            stats['uptime'] = "24h 15m"
            
            # Memory usage
            memory = psutil.virtual_memory()
            stats['memory_usage'] = f"{memory.percent:.1f}%"
            
            # Active tasks (mock - implement actual task tracking)
            stats['active_tasks'] = 0
            
            # Database size (mock)
            stats['db_size'] = "15.2 MB"
            
        except Exception:
            stats['uptime'] = "N/A"
            stats['memory_usage'] = "N/A"
            stats['active_tasks'] = 0
            stats['db_size'] = "N/A"
        
        # Performance metrics
        total_orders = stats['total_orders']
        completed_orders = stats['completed_orders']
        failed_orders = stats['failed_orders']
        
        if total_orders > 0:
            stats['success_rate'] = (completed_orders / total_orders) * 100
            stats['error_rate'] = (failed_orders / total_orders) * 100
        else:
            stats['success_rate'] = 0
            stats['error_rate'] = 0
        
        stats['avg_processing_time'] = "2.5 min"  # Mock data
        
        return stats
        
    except Exception as e:
        logger.error(f"Error getting admin statistics: {e}")
        return {
            'total_users': 0,
            'active_today': 0,
            'new_today': 0,
            'premium_users': 0,
            'banned_users': 0,
            'total_orders': 0,
            'pending_orders': 0,
            'processing_orders': 0,
            'completed_orders': 0,
            'failed_orders': 0,
            'orders_today': 0,
            'total_tokens_distributed': 0,
            'tokens_spent_today': 0,
            'tokens_earned_today': 0,
            'avg_tokens_per_user': 0,
            'ad_views_today': 0,
            'total_ad_views': 0,
            'tokens_from_ads': 0,
            'uptime': 'N/A',
            'memory_usage': 'N/A',
            'active_tasks': 0,
            'db_size': 'N/A',
            'success_rate': 0,
            'error_rate': 0,
            'avg_processing_time': 'N/A'
        }
