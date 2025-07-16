#!/usr/bin/env python3
"""
Jam Tayang Pro - Telegram Bot
Professional Social Media Engagement Service Bot

By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import asyncio
import logging
import os
import signal
import sys
import threading
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# Keep alive for Replit
try:
    from keep_alive import keep_alive
    keep_alive()
    print("✅ Keep-alive server started for Replit")
except ImportError:
    print("ℹ️ Keep-alive not available (running locally)")
except Exception as e:
    print(f"⚠️ Keep-alive error: {e}")

from src.bot.handlers import (
    start_handler, help_handler, register_handler, profile_handler,
    services_handler, token_handler, admin_handler, callback_handler
)
from src.database.database import init_database
from src.services.scheduler import TaskScheduler
from src.utils.logger import setup_logger

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logger()

class JamTayangProBot:
    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.application = None
        self.scheduler = TaskScheduler()
        self.running = False
        
    async def initialize(self):
        """Initialize bot and database"""
        try:
            # Initialize database
            await init_database()
            logger.info("Database initialized successfully")
            
            # Create application
            self.application = Application.builder().token(self.bot_token).build()
            
            # Add handlers
            self.add_handlers()
            
            # Start scheduler
            await self.scheduler.start()
            logger.info("Task scheduler started")
            
            logger.info("Bot initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize bot: {e}")
            raise
    
    def add_handlers(self):
        """Add all command and message handlers"""
        app = self.application
        
        # Command handlers
        app.add_handler(CommandHandler("start", start_handler))
        app.add_handler(CommandHandler("help", help_handler))
        app.add_handler(CommandHandler("daftar", register_handler))
        app.add_handler(CommandHandler("profil", profile_handler))
        app.add_handler(CommandHandler("layanan", services_handler))
        app.add_handler(CommandHandler("token", token_handler))
        app.add_handler(CommandHandler("admin", admin_handler))
        
        # Callback query handler
        app.add_handler(CallbackQueryHandler(callback_handler))
        
        # Message handlers
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("All handlers added successfully")
    
    async def start(self):
        """Start the bot with auto-restart capability"""
        try:
            await self.initialize()
            
            logger.info("🚀 Jam Tayang Pro Bot is starting...")
            logger.info("By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/")
            
            self.running = True
            
            # Start polling with auto-restart
            while self.running:
                try:
                    logger.info("Starting bot polling...")
                    await self.application.run_polling(
                        allowed_updates=['message', 'callback_query'],
                        drop_pending_updates=True,
                        close_loop=False
                    )
                except Exception as e:
                    if self.running:
                        logger.error(f"Polling error: {e}")
                        logger.info("Restarting bot in 5 seconds...")
                        await asyncio.sleep(5)
                        continue
                    else:
                        break
            
        except Exception as e:
            logger.error(f"Bot startup failed: {e}")
            raise
    
    async def stop(self):
        """Stop the bot gracefully"""
        try:
            self.running = False
            
            if self.scheduler:
                await self.scheduler.stop()
            
            if self.application:
                await self.application.stop()
            
            logger.info("Bot stopped gracefully")
            
        except Exception as e:
            logger.error(f"Error stopping bot: {e}")

async def handle_message(update, context):
    """Handle regular text messages"""
    try:
        from src.bot.handlers.message_handler import process_message
        await process_message(update, context)
    except Exception as e:
        logger.error(f"Error handling message: {e}")

async def main():
    """Main function with better error handling"""
    bot = JamTayangProBot()
    
    # Setup signal handlers for graceful shutdown
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}")
        bot.running = False
        asyncio.create_task(bot.stop())
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    retry_count = 0
    max_retries = 10
    
    while retry_count < max_retries:
        try:
            logger.info(f"🔄 Starting bot (attempt {retry_count + 1}/{max_retries})")
            await bot.start()
            break
        except KeyboardInterrupt:
            logger.info("Received interrupt signal")
            break
        except Exception as e:
            retry_count += 1
            logger.error(f"❌ Bot error (attempt {retry_count}): {e}")
            if retry_count < max_retries:
                logger.info(f"⏳ Retrying in 10 seconds...")
                await asyncio.sleep(10)
            else:
                logger.error("💀 Max retries reached. Bot stopping.")
                break
        finally:
            try:
                await bot.stop()
            except:
                pass

if __name__ == "__main__":
    # Check if bot token is provided
    if not os.getenv('BOT_TOKEN'):
        print("❌ BOT_TOKEN tidak ditemukan!")
        print("Silakan copy .env.example ke .env dan isi BOT_TOKEN Anda")
        print("Atau set BOT_TOKEN di Replit Secrets")
        exit(1)
    
    print("🚀 Jam Tayang Pro Bot Starting...")
    print("By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/")
    
    # Run the bot
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bot dihentikan oleh pengguna")
    except Exception as e:
        print(f"❌ Fatal Error: {e}")
        import traceback
        traceback.print_exc()
