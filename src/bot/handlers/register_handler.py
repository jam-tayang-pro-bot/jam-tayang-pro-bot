"""
Register command handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id, create_user
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_main_menu_keyboard

logger = setup_logger()

async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /daftar command"""
    try:
        user = update.effective_user
        
        # Log user action
        log_user_action(user.id, user.username, "register_command", "")
        
        # Check if user already exists
        db_user = await get_user_by_telegram_id(user.id)
        
        if db_user:
            # User already registered
            await update.message.reply_text(
                f"✅ **Anda sudah terdaftar!**\n\n"
                f"👤 **Nama:** {db_user.first_name or db_user.username}\n"
                f"💰 **Token:** {db_user.tokens} token\n"
                f"📅 **Bergabung:** {db_user.registration_date.strftime('%d/%m/%Y')}\n\n"
                f"Gunakan menu di bawah untuk mulai menggunakan layanan kami!",
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Create new user
        try:
            new_user = await create_user(
                telegram_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Registration success message
            welcome_text = f"""
🎉 **Pendaftaran Berhasil!**

Selamat datang di Jam Tayang Pro, {user.first_name or user.username}! 👋

🎁 **Bonus Pendaftaran:**
• 50 Token GRATIS sudah masuk ke akun Anda!

📊 **Informasi Akun:**
• Nama: {new_user.first_name or new_user.username}
• Token: {new_user.tokens} token
• Status: Gratis
• Bergabung: {new_user.registration_date.strftime('%d/%m/%Y')}

🚀 **Langkah Selanjutnya:**
1️⃣ Pilih platform sosial media
2️⃣ Pilih jenis layanan
3️⃣ Masukkan link konten Anda
4️⃣ Nikmati hasilnya!

💡 **Tips:**
• Tonton iklan untuk mendapatkan token gratis
• Ajak teman untuk bonus referral
• Upgrade premium untuk benefit lebih

Selamat menggunakan Jam Tayang Pro! 🎯

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
            """
            
            await update.message.reply_text(
                welcome_text,
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
            
            logger.info(f"New user registered successfully: {user.id} (@{user.username})")
            
        except Exception as e:
            logger.error(f"Error creating new user {user.id}: {e}")
            await update.message.reply_text(
                "❌ **Pendaftaran Gagal**\n\n"
                "Terjadi kesalahan saat mendaftar. Silakan coba lagi atau hubungi admin.\n\n"
                "Jika masalah berlanjut, gunakan /start untuk memulai ulang.",
                parse_mode='Markdown',
                reply_markup=get_main_menu_keyboard()
            )
    
    except Exception as e:
        logger.error(f"Error in register_handler: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan sistem. Silakan coba lagi.",
            reply_markup=get_main_menu_keyboard()
        )
