"""
Profile command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_profile_keyboard, get_main_menu_keyboard
from src.bot.utils.messages import get_profile_message

logger = setup_logger()

async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /profil command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "profile_command", "")
        
        # Get user from database
        db_user = await get_user_by_telegram_id(user.id)
        
        if not db_user:
            await update.message.reply_text(
                "❌ **Profil tidak ditemukan**\n\n"
                "Silakan gunakan /start untuk mendaftar terlebih dahulu.",
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Get user statistics
        from src.database.database import get_db_session
        from sqlalchemy import select, func
        from src.database.database import Order
        
        async with get_db_session() as session:
            # Count total orders
            result = await session.execute(
                select(func.count(Order.id)).where(Order.user_id == db_user.id)
            )
            total_orders = result.scalar() or 0
            
            # Count completed orders
            result = await session.execute(
                select(func.count(Order.id)).where(
                    Order.user_id == db_user.id,
                    Order.status == 'completed'
                )
            )
            completed_orders = result.scalar() or 0
        
        # Prepare user data
        user_data = {
            'first_name': db_user.first_name,
            'last_name': db_user.last_name,
            'username': db_user.username,
            'telegram_id': db_user.telegram_id,
            'tokens': db_user.tokens,
            'is_premium': db_user.is_premium,
            'registration_date': db_user.registration_date.strftime('%d/%m/%Y'),
            'last_active': db_user.last_active.strftime('%d/%m/%Y %H:%M'),
            'total_earned_tokens': db_user.total_earned_tokens,
            'total_spent_tokens': db_user.total_spent_tokens,
            'total_orders': total_orders,
            'completed_orders': completed_orders
        }
        
        # Create profile message
        profile_text = f"""
👤 **Profil Pengguna**

📝 **Informasi Dasar:**
• Nama: {user_data.get('first_name', 'N/A')} {user_data.get('last_name', '') or ''}
• Username: @{user_data.get('username', 'N/A')}
• Telegram ID: `{user_data.get('telegram_id')}`

💰 **Informasi Token:**
• Saldo Saat Ini: **{user_data.get('tokens', 0):,} token**
• Total Earned: {user_data.get('total_earned_tokens', 0):,} token
• Total Spent: {user_data.get('total_spent_tokens', 0):,} token

📊 **Statistik Pesanan:**
• Total Pesanan: {user_data.get('total_orders', 0):,}
• Pesanan Selesai: {user_data.get('completed_orders', 0):,}
• Success Rate: {(user_data.get('completed_orders', 0) / max(1, user_data.get('total_orders', 1)) * 100):.1f}%

🎯 **Status Akun:**
• Tipe: {'🌟 Premium' if user_data.get('is_premium') else '🆓 Gratis'}
• Bergabung: {user_data.get('registration_date')}
• Terakhir Aktif: {user_data.get('last_active')}

💡 **Tips untuk Anda:**
• Tonton iklan setiap hari untuk token gratis
• Upgrade premium untuk benefit lebih
• Ajak teman untuk bonus referral

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """
        
        await update.message.reply_text(
            profile_text,
            parse_mode='Markdown',
            reply_markup=get_profile_keyboard()
        )
        
        logger.info(f"Profile displayed for user {user.id}")
        
    except Exception as e:
        logger.error(f"Error in profile_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat menampilkan profil.",
            reply_markup=get_main_menu_keyboard()
        )
