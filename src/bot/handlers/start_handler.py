"""
Start command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id, create_user
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_main_menu_keyboard
from src.bot.utils.messages import get_welcome_message

logger = setup_logger()

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    try:
        user = update.effective_user
        chat = update.effective_chat
        
        # Log user action
        log_user_action(user.id, user.username, "start_command", f"chat_id:{chat.id}")
        
        # Get user IP (if available from webhook)
        user_ip = getattr(update, 'user_ip', None)
        
        # Check if user exists in database
        db_user = await get_user_by_telegram_id(user.id)
        
        if not db_user:
            # New user - create account
            try:
                db_user = await create_user(
                    telegram_id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    ip_address=user_ip
                )
                
                # Welcome message for new user
                welcome_text = f"""
🎉 **Selamat datang di Jam Tayang Pro!** 🎉

Halo {user.first_name or user.username}! 👋

Anda telah berhasil mendaftar dan mendapatkan:
🎁 **50 Token GRATIS** untuk memulai!

**Apa yang bisa Anda lakukan:**
📈 Tingkatkan jam tayang YouTube
❤️ Tambah likes Instagram & TikTok  
👀 Boost views semua platform
📊 Tingkatkan engagement sosial media

**Cara kerja:**
1️⃣ Pilih layanan yang diinginkan
2️⃣ Masukkan link konten Anda
3️⃣ Sistem otomatis bekerja untuk Anda
4️⃣ Lihat hasil dalam hitungan menit!

Token habis? Dapatkan lebih banyak dengan menonton iklan! 📺

Ketik /layanan untuk melihat semua layanan tersedia.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
                """
                
                keyboard = get_main_menu_keyboard()
                
                await update.message.reply_text(
                    welcome_text,
                    parse_mode='Markdown',
                    reply_markup=keyboard
                )
                
                logger.info(f"New user registered: {user.id} (@{user.username})")
                
            except Exception as e:
                logger.error(f"Error creating new user {user.id}: {e}")
                await update.message.reply_text(
                    "❌ Terjadi kesalahan saat mendaftar. Silakan coba lagi.",
                    reply_markup=get_main_menu_keyboard()
                )
                return
        
        else:
            # Existing user - show welcome back message
            welcome_text = f"""
👋 **Selamat datang kembali, {db_user.first_name or db_user.username}!**

💰 **Saldo Token:** {db_user.tokens} token
📊 **Status:** {'Premium' if db_user.is_premium else 'Gratis'}
📅 **Bergabung:** {db_user.registration_date.strftime('%d/%m/%Y')}

**Layanan Populer:**
🎬 YouTube - Jam Tayang & Subscriber
📸 Instagram - Likes & Followers  
🎵 TikTok - Views & Likes
📘 Facebook - Likes & Shares

Pilih layanan di bawah atau ketik /layanan untuk melihat semua opsi.

Token habis? Tonton iklan untuk mendapatkan token gratis! 🎁

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
            """
            
            keyboard = get_main_menu_keyboard()
            
            await update.message.reply_text(
                welcome_text,
                parse_mode='Markdown',
                reply_markup=keyboard
            )
            
            # Update last active
            from datetime import datetime
            from src.database.database import get_db_session
            async with get_db_session() as session:
                db_user.last_active = datetime.utcnow()
                await session.commit()
    
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan. Silakan coba lagi atau hubungi admin.",
            reply_markup=get_main_menu_keyboard()
        )

async def start_with_referral(update: Update, context: ContextTypes.DEFAULT_TYPE, referral_code: str):
    """Handle start command with referral code"""
    try:
        # Process referral logic here
        # For now, just call regular start handler
        await start_handler(update, context)
        
        # TODO: Implement referral bonus system
        logger.info(f"User {update.effective_user.id} started with referral: {referral_code}")
        
    except Exception as e:
        logger.error(f"Error in start_with_referral: {e}")
        await start_handler(update, context)
