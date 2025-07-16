"""
Help command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_main_menu_keyboard
from src.bot.utils.messages import get_help_message

logger = setup_logger()

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "help_command", "")
        
        # Send help message
        help_text = get_help_message()
        
        await update.message.reply_text(
            help_text,
            parse_mode='Markdown',
            reply_markup=get_main_menu_keyboard()
        )
        
        logger.info(f"Help command executed by user {user.id}")
        
    except Exception as e:
        logger.error(f"Error in help_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat menampilkan bantuan.",
            reply_markup=get_main_menu_keyboard()
        )
