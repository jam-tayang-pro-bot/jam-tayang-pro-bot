"""
Message handler for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import re
from telegram import Update
from telegram.ext import ContextTypes
from src.database.database import get_user_by_telegram_id, create_user, Order, get_db_session
from src.utils.logger import log_user_action, setup_logger
from src.bot.utils.keyboards import get_main_menu_keyboard, get_order_confirmation_keyboard
from src.bot.utils.messages import get_service_description, get_order_summary_message, get_error_message

logger = setup_logger()

async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process regular text messages"""
    try:
        user = update.effective_user
        message_text = update.message.text.strip()
        
        # Log user action
        log_user_action(user.id, user.username, "message", message_text[:100])
        
        # Get user from database
        db_user = await get_user_by_telegram_id(user.id)
        if not db_user:
            # Create user if not exists
            db_user = await create_user(
                telegram_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
        
        # Check if user is waiting for input
        if 'waiting_for_url' in context.user_data:
            await handle_url_input(update, context, db_user)
        elif 'waiting_for_quantity' in context.user_data:
            await handle_quantity_input(update, context, db_user)
        elif 'waiting_for_admin_input' in context.user_data:
            await handle_admin_input(update, context, db_user)
        else:
            # Handle general messages
            await handle_general_message(update, context, db_user)
    
    except Exception as e:
        logger.error(f"Error in process_message: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat memproses pesan Anda.",
            reply_markup=get_main_menu_keyboard()
        )

async def handle_url_input(update: Update, context: ContextTypes.DEFAULT_TYPE, db_user):
    """Handle URL input from user"""
    try:
        url = update.message.text.strip()
        service_type = context.user_data.get('waiting_for_url')
        quantity = context.user_data.get('selected_quantity')
        
        if not service_type or not quantity:
            await update.message.reply_text(
                "❌ Data pesanan tidak lengkap. Silakan mulai ulang.",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Validate URL
        if not is_valid_url(url, service_type):
            platform = service_type.split('_')[0]
            await update.message.reply_text(
                f"❌ Link {platform.title()} tidak valid. Pastikan link benar dan dapat diakses.",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Calculate cost
        service_info = get_service_description(service_type)
        cost = calculate_service_cost(service_type, quantity)
        
        # Check if user has enough tokens
        if db_user.tokens < cost:
            await update.message.reply_text(
                f"❌ Token tidak mencukupi!\n\n"
                f"Dibutuhkan: {cost} token\n"
                f"Saldo Anda: {db_user.tokens} token\n\n"
                f"Dapatkan token gratis dengan menonton iklan!",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Create order summary
        order_data = {
            'service_type': service_type,
            'service_name': service_info['name'],
            'url': url,
            'quantity': quantity,
            'cost': cost,
            'estimated_time': service_info['delivery_time']
        }
        
        # Store order data in context
        context.user_data['pending_order'] = order_data
        
        # Show order summary
        summary_message = get_order_summary_message(order_data)
        user = update.effective_user
        order_id = f"temp_{user.id}_{int(update.message.date.timestamp())}"
        
        await update.message.reply_text(
            summary_message,
            parse_mode='Markdown',
            reply_markup=get_order_confirmation_keyboard(order_id)
        )
        
        # Clear waiting state
        context.user_data.pop('waiting_for_url', None)
        context.user_data.pop('selected_quantity', None)
        
    except Exception as e:
        logger.error(f"Error handling URL input: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat memproses URL.",
            reply_markup=get_main_menu_keyboard()
        )

async def handle_quantity_input(update: Update, context: ContextTypes.DEFAULT_TYPE, db_user):
    """Handle custom quantity input"""
    try:
        quantity_text = update.message.text.strip()
        service_type = context.user_data.get('waiting_for_quantity')
        
        if not service_type:
            await update.message.reply_text(
                "❌ Data layanan tidak ditemukan. Silakan mulai ulang.",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Validate quantity
        try:
            quantity = int(quantity_text.replace(',', '').replace('.', ''))
        except ValueError:
            await update.message.reply_text(
                "❌ Jumlah harus berupa angka. Contoh: 1000",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Check min/max limits
        service_info = get_service_description(service_type)
        if quantity < service_info['min_order']:
            await update.message.reply_text(
                f"❌ Jumlah minimum: {service_info['min_order']:,}",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        if quantity > service_info['max_order']:
            await update.message.reply_text(
                f"❌ Jumlah maksimum: {service_info['max_order']:,}",
                reply_markup=get_main_menu_keyboard()
            )
            return
        
        # Store quantity and ask for URL
        context.user_data['selected_quantity'] = quantity
        context.user_data['waiting_for_url'] = service_type
        context.user_data.pop('waiting_for_quantity', None)
        
        await update.message.reply_text(
            f"🔗 **Masukkan Link**\n\n"
            f"Paste link konten Anda di sini:\n\n"
            f"**Layanan:** {service_info['name']}\n"
            f"**Jumlah:** {quantity:,}\n"
            f"**Biaya:** {calculate_service_cost(service_type, quantity)} token",
            parse_mode='Markdown'
        )
        
    except Exception as e:
        logger.error(f"Error handling quantity input: {e}")
        await update.message.reply_text(
            "❌ Terjadi kesalahan saat memproses jumlah.",
            reply_markup=get_main_menu_keyboard()
        )

async def handle_admin_input(update: Update, context: ContextTypes.DEFAULT_TYPE, db_user):
    """Handle admin command input"""
    # Check if user is admin
    import os
    admin_ids = os.getenv('ADMIN_USER_IDS', '').split(',')
    
    if str(db_user.telegram_id) not in admin_ids:
        await update.message.reply_text("❌ Akses ditolak.")
        return
    
    # TODO: Implement admin command processing
    await update.message.reply_text(
        "🔧 Admin command processed.",
        reply_markup=get_main_menu_keyboard()
    )
    
    context.user_data.pop('waiting_for_admin_input', None)

async def handle_general_message(update: Update, context: ContextTypes.DEFAULT_TYPE, db_user):
    """Handle general messages and commands"""
    message_text = update.message.text.lower().strip()
    
    # Handle common keywords
    if any(keyword in message_text for keyword in ['halo', 'hai', 'hello', 'hi']):
        await update.message.reply_text(
            f"👋 Halo {db_user.first_name or db_user.username}!\n\n"
            f"Selamat datang di Jam Tayang Pro. Pilih layanan yang Anda butuhkan:",
            reply_markup=get_main_menu_keyboard()
        )
    
    elif any(keyword in message_text for keyword in ['bantuan', 'help', 'tolong']):
        from src.bot.utils.messages import get_help_message
        await update.message.reply_text(
            get_help_message(),
            parse_mode='Markdown',
            reply_markup=get_main_menu_keyboard()
        )
    
    elif any(keyword in message_text for keyword in ['token', 'saldo', 'balance']):
        await update.message.reply_text(
            f"💰 **Saldo Token Anda**\n\n"
            f"Token: {db_user.tokens:,}\n"
            f"Total Earned: {db_user.total_earned_tokens:,}\n"
            f"Total Spent: {db_user.total_spent_tokens:,}\n\n"
            f"Dapatkan token gratis dengan menonton iklan!",
            parse_mode='Markdown',
            reply_markup=get_main_menu_keyboard()
        )
    
    elif any(keyword in message_text for keyword in ['harga', 'price', 'biaya', 'cost']):
        await update.message.reply_text(
            "💰 **Daftar Harga Layanan**\n\n"
            "🎬 **YouTube:**\n"
            "• Jam Tayang: 1 token = 1 menit\n"
            "• Subscriber: 1 token = 1 subscriber\n"
            "• Likes: 1 token = 5 likes\n\n"
            "📸 **Instagram:**\n"
            "• Likes: 1 token = 10 likes\n"
            "• Followers: 1 token = 1 follower\n\n"
            "🎵 **TikTok:**\n"
            "• Views: 1 token = 100 views\n"
            "• Likes: 1 token = 5 likes\n\n"
            "Pilih layanan untuk detail lengkap!",
            parse_mode='Markdown',
            reply_markup=get_main_menu_keyboard()
        )
    
    else:
        # Default response for unrecognized messages
        await update.message.reply_text(
            "🤖 Maaf, saya tidak mengerti pesan Anda.\n\n"
            "Gunakan menu di bawah atau ketik /help untuk bantuan:",
            reply_markup=get_main_menu_keyboard()
        )

def is_valid_url(url: str, service_type: str) -> bool:
    """Validate URL based on service type"""
    try:
        # Basic URL validation
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if not url_pattern.match(url):
            return False
        
        # Platform-specific validation
        platform = service_type.split('_')[0]
        
        if platform == 'youtube':
            return any(domain in url.lower() for domain in ['youtube.com', 'youtu.be'])
        elif platform == 'instagram':
            return 'instagram.com' in url.lower()
        elif platform == 'tiktok':
            return any(domain in url.lower() for domain in ['tiktok.com', 'vm.tiktok.com'])
        elif platform == 'facebook':
            return any(domain in url.lower() for domain in ['facebook.com', 'fb.com'])
        
        return True
        
    except Exception:
        return False

def calculate_service_cost(service_type: str, quantity: int) -> int:
    """Calculate service cost in tokens"""
    # Service pricing (tokens per unit)
    pricing = {
        'youtube_watchtime': 1,      # 1 token = 1 minute
        'youtube_subscribers': 1,     # 1 token = 1 subscriber
        'youtube_likes': 0.2,        # 1 token = 5 likes
        'youtube_views': 0.01,       # 1 token = 100 views
        'youtube_comments': 2,       # 1 token = 0.5 comments
        
        'instagram_likes': 0.1,      # 1 token = 10 likes
        'instagram_followers': 1,    # 1 token = 1 follower
        'instagram_views': 0.01,     # 1 token = 100 views
        'instagram_comments': 2,     # 1 token = 0.5 comments
        'instagram_story_views': 0.02, # 1 token = 50 story views
        
        'tiktok_views': 0.01,        # 1 token = 100 views
        'tiktok_likes': 0.2,         # 1 token = 5 likes
        'tiktok_followers': 1,       # 1 token = 1 follower
        'tiktok_comments': 2,        # 1 token = 0.5 comments
        'tiktok_shares': 0.5,        # 1 token = 2 shares
        
        'facebook_likes': 0.1,       # 1 token = 10 likes
        'facebook_followers': 1,     # 1 token = 1 follower
        'facebook_shares': 0.5,      # 1 token = 2 shares
        'facebook_comments': 2,      # 1 token = 0.5 comments
        'facebook_views': 0.01,      # 1 token = 100 views
    }
    
    rate = pricing.get(service_type, 1)
    cost = int(quantity * rate)
    
    # Minimum cost is 1 token
    return max(1, cost)

async def create_order_from_data(order_data: dict, user_id: int) -> Order:
    """Create order in database"""
    async with get_db_session() as session:
        order = Order(
            user_id=user_id,
            service_type=order_data['service_type'],
            platform=order_data['service_type'].split('_')[0],
            target_url=order_data['url'],
            quantity=order_data['quantity'],
            tokens_cost=order_data['cost'],
            status='pending'
        )
        
        session.add(order)
        await session.commit()
        await session.refresh(order)
        
        return order
