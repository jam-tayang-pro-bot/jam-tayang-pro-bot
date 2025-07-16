"""
Callback query handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import (
    get_main_menu_keyboard, get_youtube_services_keyboard, get_instagram_services_keyboard,
    get_tiktok_services_keyboard, get_facebook_services_keyboard, get_quantity_keyboard,
    get_token_menu_keyboard, get_profile_keyboard, get_ad_watch_keyboard,
    get_cancel_keyboard, get_support_keyboard
)
from src.bot.utils.messages import (
    get_token_info_message, get_profile_message, get_ad_watch_message,
    get_help_message, format_service_message, get_service_description
)

logger = setup_logger()

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all callback queries"""
    try:
        query = update.callback_query
        user = update.effective_user
        data = query.data
        
        # Answer callback query to remove loading state
        await query.answer()
        
        # Log user action
        log_user_action(user.id, user.username, "callback_query", data)
        
        # Get user from database
        db_user = await get_user_by_telegram_id(user.id)
        if not db_user:
            await query.edit_message_text("❌ User tidak ditemukan. Silakan /start ulang.")
            return
        
        # Route callback based on data
        if data == "back_to_main":
            await handle_back_to_main(query, context, db_user)
        
        elif data.startswith("service_"):
            await handle_service_selection(query, context, data, db_user)
        
        elif data.startswith("youtube_"):
            await handle_youtube_service(query, context, data, db_user)
        
        elif data.startswith("instagram_"):
            await handle_instagram_service(query, context, data, db_user)
        
        elif data.startswith("tiktok_"):
            await handle_tiktok_service(query, context, data, db_user)
        
        elif data.startswith("facebook_"):
            await handle_facebook_service(query, context, data, db_user)
        
        elif data == "my_tokens":
            await handle_token_info(query, context, db_user)
        
        elif data == "my_profile":
            await handle_profile_info(query, context, db_user)
        
        elif data == "my_orders":
            await handle_my_orders(query, context, db_user)
        
        elif data == "earn_tokens":
            await handle_earn_tokens(query, context, db_user)
        
        elif data == "watch_ads":
            await handle_watch_ads(query, context, db_user)
        
        elif data.startswith("ad_completed_"):
            await handle_ad_completed(query, context, data, db_user)
        
        elif data.startswith("qty_"):
            await handle_quantity_selection(query, context, data, db_user)
        
        elif data.startswith("confirm_order_"):
            await handle_order_confirmation(query, context, data, db_user)
        
        elif data.startswith("cancel_order_"):
            await handle_order_cancellation(query, context, data, db_user)
        
        elif data == "help":
            await handle_help(query, context)
        
        elif data == "support":
            await handle_support(query, context)
        
        elif data.startswith("admin_"):
            await handle_admin_callbacks(query, context, data, db_user)
        
        else:
            await query.edit_message_text("❌ Perintah tidak dikenali.")
    
    except Exception as e:
        logger.error(f"Error in callback_handler: {e}")
        try:
            await query.edit_message_text("❌ Terjadi kesalahan. Silakan coba lagi.")
        except:
            pass

async def handle_back_to_main(query, context, db_user):
    """Handle back to main menu"""
    welcome_text = f"""
👋 **Selamat datang kembali, {db_user.first_name or db_user.username}!**

💰 **Saldo Token:** {db_user.tokens} token
📊 **Status:** {'Premium' if db_user.is_premium else 'Gratis'}

**Layanan Populer:**
🎬 YouTube - Jam Tayang & Subscriber
📸 Instagram - Likes & Followers  
🎵 TikTok - Views & Likes
📘 Facebook - Likes & Shares

Pilih layanan di bawah atau ketik /layanan untuk melihat semua opsi.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """
    
    await query.edit_message_text(
        welcome_text,
        parse_mode='Markdown',
        reply_markup=get_main_menu_keyboard()
    )

async def handle_service_selection(query, context, data, db_user):
    """Handle service platform selection"""
    platform = data.replace("service_", "")
    
    if platform == "youtube":
        text = """
🎬 **YouTube Services**

Tingkatkan performa channel YouTube Anda dengan layanan berkualitas tinggi:

⏰ **Jam Tayang** - Untuk monetisasi
👥 **Subscriber** - Tingkatkan kredibilitas
👍 **Likes** - Boost engagement
👀 **Views** - Viral content
💬 **Komentar** - Interaksi aktif
🔔 **Notifikasi** - Subscriber aktif

Semua layanan aman dan sesuai ToS YouTube!
        """
        keyboard = get_youtube_services_keyboard()
    
    elif platform == "instagram":
        text = """
📸 **Instagram Services**

Boost engagement Instagram Anda dengan layanan premium:

❤️ **Likes** - Tingkatkan engagement
👥 **Followers** - Perbesar audience
👀 **Views** - Video & Reels viral
💬 **Komentar** - Interaksi natural
📖 **Story Views** - Jangkauan luas
💾 **Saves** - Konten berkualitas

100% real accounts dengan profile lengkap!
        """
        keyboard = get_instagram_services_keyboard()
    
    elif platform == "tiktok":
        text = """
🎵 **TikTok Services**

Viral di TikTok dengan layanan terbaik:

👀 **Views** - Masuk FYP
❤️ **Likes** - Boost algoritma
👥 **Followers** - Bangun fanbase
💬 **Komentar** - Engagement tinggi
🔄 **Shares** - Konten viral
📥 **Downloads** - Popularitas

Semua dari user aktif TikTok Indonesia!
        """
        keyboard = get_tiktok_services_keyboard()
    
    elif platform == "facebook":
        text = """
📘 **Facebook Services**

Tingkatkan presence Facebook Anda:

👍 **Likes** - Post engagement
👥 **Followers** - Profile followers
🔄 **Shares** - Viral content
💬 **Komentar** - Interaksi aktif
👀 **Views** - Video views
📄 **Page Likes** - Business page

Dari akun Facebook real dan aktif!
        """
        keyboard = get_facebook_services_keyboard()
    
    else:
        text = "❌ Platform tidak ditemukan."
        keyboard = get_main_menu_keyboard()
    
    await query.edit_message_text(
        text,
        parse_mode='Markdown',
        reply_markup=keyboard
    )

async def handle_youtube_service(query, context, data, db_user):
    """Handle YouTube service selection"""
    service = data.replace("youtube_", "")
    service_type = f"youtube_{service}"
    
    # Store service selection in user context
    context.user_data['selected_service'] = service_type
    
    message = format_service_message(service_type)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_quantity_keyboard(service_type)
    )

async def handle_instagram_service(query, context, data, db_user):
    """Handle Instagram service selection"""
    service = data.replace("instagram_", "")
    service_type = f"instagram_{service}"
    
    context.user_data['selected_service'] = service_type
    
    message = format_service_message(service_type)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_quantity_keyboard(service_type)
    )

async def handle_tiktok_service(query, context, data, db_user):
    """Handle TikTok service selection"""
    service = data.replace("tiktok_", "")
    service_type = f"tiktok_{service}"
    
    context.user_data['selected_service'] = service_type
    
    message = format_service_message(service_type)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_quantity_keyboard(service_type)
    )

async def handle_facebook_service(query, context, data, db_user):
    """Handle Facebook service selection"""
    service = data.replace("facebook_", "")
    service_type = f"facebook_{service}"
    
    context.user_data['selected_service'] = service_type
    
    message = format_service_message(service_type)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_quantity_keyboard(service_type)
    )

async def handle_token_info(query, context, db_user):
    """Handle token information display"""
    user_data = {
        'tokens': db_user.tokens,
        'total_earned_tokens': db_user.total_earned_tokens,
        'total_spent_tokens': db_user.total_spent_tokens
    }
    
    message = get_token_info_message(user_data)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_token_menu_keyboard()
    )

async def handle_profile_info(query, context, db_user):
    """Handle profile information display"""
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
        'total_orders': 0  # TODO: Calculate from orders
    }
    
    message = get_profile_message(user_data)
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_profile_keyboard()
    )

async def handle_my_orders(query, context, db_user):
    """Handle my orders display"""
    # TODO: Implement order history display
    message = """
📋 **Pesanan Saya**

Belum ada pesanan yang dibuat.

Mulai dengan memilih layanan dari menu utama!

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_main_menu_keyboard()
    )

async def handle_earn_tokens(query, context, db_user):
    """Handle earn tokens menu"""
    message = """
🎁 **Dapatkan Token Gratis**

**Cara Mendapatkan Token:**

📺 **Tonton Iklan** (5 token/iklan)
• Tonton iklan selama 30-60 detik
• Maksimal 20 iklan per hari
• Total 100 token gratis per hari!

🎯 **Tugas Harian** (10-50 token)
• Login harian: 5 token
• Share bot: 10 token
• Review positif: 25 token

👥 **Referral** (25 token/orang)
• Ajak teman pakai bot
• Dapatkan 25 token per referral
• Teman juga dapat bonus 10 token

💎 **Upgrade Premium** (500 token bonus)
• Akses layanan premium
• Token bonus 500
• Prioritas support

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_token_menu_keyboard()
    )

async def handle_watch_ads(query, context, db_user):
    """Handle watch ads"""
    # TODO: Implement ad watching system
    ad_data = {
        'reward': 5,
        'duration': 30,
        'watched_today': 0,
        'daily_limit': 20
    }
    
    message = get_ad_watch_message(ad_data)
    
    # Mock ad URL - replace with real ad system
    ad_url = "https://www.kantongaplikasi.com/ads/sample"
    keyboard = get_ad_watch_keyboard(ad_url, "sample_ad_123")
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=keyboard
    )

async def handle_ad_completed(query, context, data, db_user):
    """Handle ad completion"""
    ad_id = data.replace("ad_completed_", "")
    
    # TODO: Verify ad was actually watched
    # For now, just give tokens
    
    from src.database.database import update_user_tokens
    
    try:
        new_balance = await update_user_tokens(
            user_id=db_user.id,
            amount=5,
            transaction_type="earned",
            source="ad_view",
            description=f"Menonton iklan {ad_id}",
            reference_id=ad_id
        )
        
        message = f"""
✅ **Iklan Selesai Ditonton!**

🎁 **Token Earned:** +5 token
💰 **Saldo Baru:** {new_balance} token

Terima kasih telah menonton iklan!
Anda bisa menonton iklan lagi untuk mendapatkan lebih banyak token.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """
        
        await query.edit_message_text(
            message,
            parse_mode='Markdown',
            reply_markup=get_token_menu_keyboard()
        )
        
    except Exception as e:
        logger.error(f"Error processing ad completion: {e}")
        await query.edit_message_text(
            "❌ Terjadi kesalahan saat memproses reward. Silakan coba lagi.",
            reply_markup=get_token_menu_keyboard()
        )

async def handle_quantity_selection(query, context, data, db_user):
    """Handle quantity selection"""
    # Parse data: qty_servicetype_quantity
    parts = data.split("_")
    if len(parts) < 3:
        await query.edit_message_text("❌ Data tidak valid.")
        return
    
    service_type = "_".join(parts[1:-1])
    quantity = parts[-1]
    
    if quantity == "custom":
        # Ask user to input custom quantity
        await query.edit_message_text(
            "✏️ **Masukkan Jumlah Custom**\n\nKetik jumlah yang Anda inginkan:",
            reply_markup=get_cancel_keyboard()
        )
        context.user_data['waiting_for_quantity'] = service_type
        return
    
    try:
        quantity = int(quantity)
        context.user_data['selected_quantity'] = quantity
        
        # Ask for URL
        await query.edit_message_text(
            f"🔗 **Masukkan Link**\n\nPaste link konten Anda di sini:\n\n**Layanan:** {get_service_description(service_type)['name']}\n**Jumlah:** {quantity:,}",
            reply_markup=get_cancel_keyboard()
        )
        context.user_data['waiting_for_url'] = service_type
        
    except ValueError:
        await query.edit_message_text("❌ Jumlah tidak valid.")

async def handle_help(query, context):
    """Handle help display"""
    message = get_help_message()
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_main_menu_keyboard()
    )

async def handle_support(query, context):
    """Handle support menu"""
    message = """
📞 **Support Jam Tayang Pro**

Butuh bantuan? Kami siap membantu Anda 24/7!

**Kontak Support:**
💬 Live Chat: Tersedia di website
📧 Email: support@kantongaplikasi.com
📱 Telegram: @kantongaplikasi
🌐 Website: kantongaplikasi.com

**Jam Operasional:**
🕐 24/7 untuk chat & email
📞 08:00 - 22:00 WIB untuk telepon

**Response Time:**
• Live Chat: < 5 menit
• Email: < 2 jam
• Telegram: < 10 menit

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """
    
    await query.edit_message_text(
        message,
        parse_mode='Markdown',
        reply_markup=get_support_keyboard()
    )

async def handle_admin_callbacks(query, context, data, db_user):
    """Handle admin panel callbacks"""
    # Check if user is admin
    import os
    admin_ids = os.getenv('ADMIN_USER_IDS', '').split(',')
    
    if str(db_user.telegram_id) not in admin_ids:
        await query.edit_message_text("❌ Akses ditolak.")
        return
    
    # TODO: Implement admin panel functionality
    await query.edit_message_text(
        "🔧 **Admin Panel**\n\nFitur admin sedang dalam pengembangan.",
        reply_markup=get_main_menu_keyboard()
    )

async def handle_order_confirmation(query, context, data, db_user):
    """Handle order confirmation"""
    # TODO: Implement order confirmation logic
    order_id = data.replace("confirm_order_", "")
    
    await query.edit_message_text(
        f"✅ **Pesanan Dikonfirmasi**\n\nPesanan #{order_id} sedang diproses.\nAnda akan mendapat notifikasi saat selesai.",
        reply_markup=get_main_menu_keyboard()
    )

async def handle_order_cancellation(query, context, data, db_user):
    """Handle order cancellation"""
    # TODO: Implement order cancellation logic
    order_id = data.replace("cancel_order_", "")
    
    await query.edit_message_text(
        f"❌ **Pesanan Dibatalkan**\n\nPesanan #{order_id} telah dibatalkan.\nToken akan dikembalikan ke akun Anda.",
        reply_markup=get_main_menu_keyboard()
    )
