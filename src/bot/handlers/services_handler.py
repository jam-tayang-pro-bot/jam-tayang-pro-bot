"""
Services command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_main_menu_keyboard

logger = setup_logger()

async def services_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /layanan command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "services_command", "")
        
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
        
        # Services overview message
        services_text = f"""
🎯 **Layanan Jam Tayang Pro**

Tingkatkan engagement sosial media Anda dengan layanan berkualitas tinggi!

🎬 **YOUTUBE SERVICES**
⏰ **Jam Tayang** - 1 token = 1 menit
• Untuk monetisasi channel
• Viewer real dari Indonesia & Global
• Retention rate 80%+
• Aman untuk AdSense

👥 **Subscriber** - 1 token = 1 subscriber
• Subscriber real & aktif
• Profile lengkap dengan foto
• Tidak akan unsubscribe
• Garansi lifetime

👍 **Likes** - 1 token = 5 likes
• Dari akun YouTube aktif
• Boost algoritma YouTube
• Delivery cepat & aman

👀 **Views** - 1 token = 100 views
• Views berkualitas tinggi
• Retention rate 90%+
• Boost ranking video

📸 **INSTAGRAM SERVICES**
❤️ **Likes** - 1 token = 10 likes
• Dari akun Instagram real
• Profile foto & bio lengkap
• Garansi refill 60 hari

👥 **Followers** - 1 token = 1 follower
• Followers aktif & engaged
• Profile lengkap dengan postingan
• Aman dari shadowban

👀 **Views** - 1 token = 100 views
• Views video & reels
• Boost algoritma Instagram
• Delivery super cepat

🎵 **TIKTOK SERVICES**
👀 **Views** - 1 token = 100 views
• Views dari user real
• Boost masuk FYP
• Retention rate 90%+

❤️ **Likes** - 1 token = 5 likes
• Dari akun TikTok aktif
• Profile lengkap & verified
• Boost engagement rate

👥 **Followers** - 1 token = 1 follower
• Followers aktif Indonesia
• Engagement rate tinggi
• Garansi 90 hari

📘 **FACEBOOK SERVICES**
👍 **Likes** - 1 token = 10 likes
• Dari akun Facebook real
• Profile lengkap dengan foto
• Boost organic reach

👥 **Followers** - 1 token = 1 follower
• Followers aktif & engaged
• Profile lengkap dengan postingan
• Aman dari algoritma Facebook

🔄 **Shares** - 1 token = 2 shares
• Share dari akun real
• Boost viral content
• Tingkatkan jangkauan

💰 **Saldo Token Anda:** {db_user.tokens:,} token

🎁 **Cara Mendapatkan Token:**
• Tonton iklan (5 token/iklan)
• Tugas harian (10-50 token)
• Referral bonus (25 token)
• Upgrade premium (bonus 500 token)

✨ **Keunggulan Kami:**
• ✅ 100% Real & Aktif
• ✅ Delivery Cepat (5 menit - 12 jam)
• ✅ Garansi Refill/Replacement
• ✅ Aman dari Algoritma Platform
• ✅ Support 24/7
• ✅ Harga Terjangkau

Pilih platform di menu utama untuk mulai order!

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """
        
        await update.message.reply_text(
            services_text,
            parse_mode='Markdown',
            reply_markup=get_main_menu_keyboard()
        )
        
        logger.info(f"Services list displayed for user {user.id}")
        
    except Exception as e:
        logger.error(f"Error in services_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat menampilkan layanan.",
            reply_markup=get_main_menu_keyboard()
        )
