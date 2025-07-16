"""
Keyboard utilities for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard():
    """Get main menu inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("🎬 YouTube", callback_data="service_youtube"),
            InlineKeyboardButton("📸 Instagram", callback_data="service_instagram")
        ],
        [
            InlineKeyboardButton("🎵 TikTok", callback_data="service_tiktok"),
            InlineKeyboardButton("📘 Facebook", callback_data="service_facebook")
        ],
        [
            InlineKeyboardButton("💰 Token Saya", callback_data="my_tokens"),
            InlineKeyboardButton("📊 Profil", callback_data="my_profile")
        ],
        [
            InlineKeyboardButton("🎁 Dapatkan Token", callback_data="earn_tokens"),
            InlineKeyboardButton("📋 Pesanan Saya", callback_data="my_orders")
        ],
        [
            InlineKeyboardButton("❓ Bantuan", callback_data="help"),
            InlineKeyboardButton("📞 Support", callback_data="support")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_youtube_services_keyboard():
    """Get YouTube services keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("⏰ Jam Tayang", callback_data="youtube_watchtime"),
            InlineKeyboardButton("👥 Subscriber", callback_data="youtube_subscribers")
        ],
        [
            InlineKeyboardButton("👍 Likes", callback_data="youtube_likes"),
            InlineKeyboardButton("👀 Views", callback_data="youtube_views")
        ],
        [
            InlineKeyboardButton("💬 Komentar", callback_data="youtube_comments"),
            InlineKeyboardButton("🔔 Notifikasi", callback_data="youtube_notifications")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_instagram_services_keyboard():
    """Get Instagram services keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("❤️ Likes", callback_data="instagram_likes"),
            InlineKeyboardButton("👥 Followers", callback_data="instagram_followers")
        ],
        [
            InlineKeyboardButton("👀 Views", callback_data="instagram_views"),
            InlineKeyboardButton("💬 Komentar", callback_data="instagram_comments")
        ],
        [
            InlineKeyboardButton("📖 Story Views", callback_data="instagram_story_views"),
            InlineKeyboardButton("💾 Saves", callback_data="instagram_saves")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_tiktok_services_keyboard():
    """Get TikTok services keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("👀 Views", callback_data="tiktok_views"),
            InlineKeyboardButton("❤️ Likes", callback_data="tiktok_likes")
        ],
        [
            InlineKeyboardButton("👥 Followers", callback_data="tiktok_followers"),
            InlineKeyboardButton("💬 Komentar", callback_data="tiktok_comments")
        ],
        [
            InlineKeyboardButton("🔄 Shares", callback_data="tiktok_shares"),
            InlineKeyboardButton("📥 Downloads", callback_data="tiktok_downloads")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_facebook_services_keyboard():
    """Get Facebook services keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("👍 Likes", callback_data="facebook_likes"),
            InlineKeyboardButton("👥 Followers", callback_data="facebook_followers")
        ],
        [
            InlineKeyboardButton("🔄 Shares", callback_data="facebook_shares"),
            InlineKeyboardButton("💬 Komentar", callback_data="facebook_comments")
        ],
        [
            InlineKeyboardButton("👀 Views", callback_data="facebook_views"),
            InlineKeyboardButton("📄 Page Likes", callback_data="facebook_page_likes")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_token_menu_keyboard():
    """Get token management keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("🎁 Tonton Iklan", callback_data="watch_ads"),
            InlineKeyboardButton("📊 Riwayat Token", callback_data="token_history")
        ],
        [
            InlineKeyboardButton("💎 Upgrade Premium", callback_data="upgrade_premium"),
            InlineKeyboardButton("🎯 Tugas Harian", callback_data="daily_tasks")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_order_confirmation_keyboard(order_id: str):
    """Get order confirmation keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("✅ Konfirmasi", callback_data=f"confirm_order_{order_id}"),
            InlineKeyboardButton("❌ Batal", callback_data=f"cancel_order_{order_id}")
        ],
        [
            InlineKeyboardButton("📝 Edit", callback_data=f"edit_order_{order_id}"),
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_quantity_keyboard(service_type: str):
    """Get quantity selection keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("100", callback_data=f"qty_{service_type}_100"),
            InlineKeyboardButton("500", callback_data=f"qty_{service_type}_500"),
            InlineKeyboardButton("1000", callback_data=f"qty_{service_type}_1000")
        ],
        [
            InlineKeyboardButton("2500", callback_data=f"qty_{service_type}_2500"),
            InlineKeyboardButton("5000", callback_data=f"qty_{service_type}_5000"),
            InlineKeyboardButton("10000", callback_data=f"qty_{service_type}_10000")
        ],
        [
            InlineKeyboardButton("✏️ Custom", callback_data=f"qty_{service_type}_custom"),
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_services")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_keyboard():
    """Get admin panel keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("👥 Users", callback_data="admin_users"),
            InlineKeyboardButton("📊 Stats", callback_data="admin_stats")
        ],
        [
            InlineKeyboardButton("💰 Tokens", callback_data="admin_tokens"),
            InlineKeyboardButton("📋 Orders", callback_data="admin_orders")
        ],
        [
            InlineKeyboardButton("⚙️ Config", callback_data="admin_config"),
            InlineKeyboardButton("🔧 System", callback_data="admin_system")
        ],
        [
            InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast"),
            InlineKeyboardButton("🚫 Ban User", callback_data="admin_ban")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_ad_watch_keyboard(ad_url: str, ad_id: str):
    """Get advertisement watch keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📺 Tonton Iklan", url=ad_url)
        ],
        [
            InlineKeyboardButton("✅ Selesai Menonton", callback_data=f"ad_completed_{ad_id}"),
            InlineKeyboardButton("❌ Batal", callback_data="cancel_ad")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_profile_keyboard():
    """Get user profile keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📝 Edit Profil", callback_data="edit_profile"),
            InlineKeyboardButton("🔄 Refresh", callback_data="refresh_profile")
        ],
        [
            InlineKeyboardButton("📊 Statistik", callback_data="user_stats"),
            InlineKeyboardButton("🎯 Achievement", callback_data="user_achievements")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_support_keyboard():
    """Get support keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("💬 Live Chat", callback_data="live_chat"),
            InlineKeyboardButton("📧 Email", callback_data="email_support")
        ],
        [
            InlineKeyboardButton("❓ FAQ", callback_data="faq"),
            InlineKeyboardButton("📖 Tutorial", callback_data="tutorial")
        ],
        [
            InlineKeyboardButton("🌐 Website", url="https://www.kantongaplikasi.com/"),
            InlineKeyboardButton("📱 Telegram", url="https://t.me/kantongaplikasi")
        ],
        [
            InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_cancel_keyboard():
    """Get cancel operation keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("❌ Batal", callback_data="cancel_operation")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_yes_no_keyboard(action: str):
    """Get yes/no confirmation keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("✅ Ya", callback_data=f"yes_{action}"),
            InlineKeyboardButton("❌ Tidak", callback_data=f"no_{action}")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_pagination_keyboard(current_page: int, total_pages: int, callback_prefix: str):
    """Get pagination keyboard"""
    keyboard = []
    
    # Navigation buttons
    nav_buttons = []
    if current_page > 1:
        nav_buttons.append(InlineKeyboardButton("⬅️", callback_data=f"{callback_prefix}_page_{current_page-1}"))
    
    nav_buttons.append(InlineKeyboardButton(f"{current_page}/{total_pages}", callback_data="current_page"))
    
    if current_page < total_pages:
        nav_buttons.append(InlineKeyboardButton("➡️", callback_data=f"{callback_prefix}_page_{current_page+1}"))
    
    keyboard.append(nav_buttons)
    
    # Back button
    keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")])
    
    return InlineKeyboardMarkup(keyboard)
