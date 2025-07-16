"""
Token command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id, get_db_session, TokenTransaction
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_token_menu_keyboard, get_main_menu_keyboard
from src.bot.utils.messages import get_token_info_message

logger = setup_logger()

async def token_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /token command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "token_command", "")
        
        # Get user from database
        db_user = await get_user_by_telegram_id(user.id)
        
        if not db_user:
            await update.message.reply_text(
                "❌ **Akun tidak ditemukan**\n\n"
                "Silakan gunakan /start untuk mendaftar terlebih dahulu.",
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Get recent token transactions
        from sqlalchemy import select, desc
        
        async with get_db_session() as session:
            result = await session.execute(
                select(TokenTransaction)
                .where(TokenTransaction.user_id == db_user.id)
                .order_by(desc(TokenTransaction.created_at))
                .limit(5)
            )
            recent_transactions = result.scalars().all()
        
        # Format recent transactions
        transaction_text = ""
        if recent_transactions:
            transaction_text = "\n📊 **Transaksi Terakhir:**\n"
            for tx in recent_transactions:
                emoji = "➕" if tx.amount > 0 else "➖"
                date_str = tx.created_at.strftime('%d/%m %H:%M')
                transaction_text += f"• {emoji} {abs(tx.amount)} token - {tx.description} ({date_str})\n"
        
        # Token information message
        token_text = f"""
💰 **Informasi Token**

💎 **Saldo Saat Ini:** {db_user.tokens:,} token

📈 **Statistik Token:**
• Total Earned: {db_user.total_earned_tokens:,} token
• Total Spent: {db_user.total_spent_tokens:,} token
• Registration Bonus: 50 token
• Net Balance: {db_user.total_earned_tokens - db_user.total_spent_tokens:,} token

{transaction_text}

🎁 **Cara Mendapatkan Token Gratis:**

📺 **Tonton Iklan** (5 token/iklan)
• Durasi: 30-60 detik
• Maksimal: 20 iklan/hari
• Potensi: 100 token/hari

🎯 **Tugas Harian:**
• Login harian: 5 token
• Share ke grup: 10 token
• Review positif: 25 token
• Invite teman: 15 token

👥 **Program Referral:**
• Ajak teman: 25 token/referral
• Teman dapat: 10 token bonus
• Unlimited referrals!

💎 **Upgrade Premium:**
• Bonus: 500 token
• Daily bonus: 20 token
• Exclusive services
• Priority support

💡 **Tips Menghemat Token:**
• Pilih paket besar untuk efisiensi
• Manfaatkan promo dan diskon
• Gabungkan beberapa layanan
• Upgrade premium untuk bonus

📊 **Nilai Token:**
1 token = Rp 100 (estimasi)
Saldo Anda ≈ Rp {db_user.tokens * 100:,}

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """
        
        await update.message.reply_text(
            token_text,
            parse_mode='Markdown',
            reply_markup=get_token_menu_keyboard()
        )
        
        logger.info(f"Token info displayed for user {user.id}")
        
    except Exception as e:
        logger.error(f"Error in token_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat menampilkan informasi token.",
            reply_markup=get_main_menu_keyboard()
        )
