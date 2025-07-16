"""
Message templates for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

from datetime import datetime
from typing import Dict, Any

def get_welcome_message(user_name: str, is_new_user: bool = False) -> str:
    """Get welcome message for users"""
    if is_new_user:
        return f"""
🎉 **Selamat datang di Jam Tayang Pro!** 🎉

Halo {user_name}! 👋

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

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """
    else:
        return f"""
👋 **Selamat datang kembali, {user_name}!**

Siap untuk meningkatkan engagement sosial media Anda hari ini?

Pilih layanan di bawah atau ketik /layanan untuk melihat semua opsi.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
        """

def get_service_description(service_type: str) -> Dict[str, Any]:
    """Get service description and pricing"""
    services = {
        "youtube_watchtime": {
            "name": "⏰ Jam Tayang YouTube",
            "description": "Tingkatkan jam tayang video YouTube Anda dengan viewer real dan berkualitas",
            "features": [
                "✅ Viewer dari Indonesia & Global",
                "✅ Retention rate tinggi (80%+)",
                "✅ Aman untuk monetisasi",
                "✅ Gradual delivery",
                "✅ Garansi refill 30 hari"
            ],
            "pricing": "1 token = 1 menit jam tayang",
            "min_order": 60,
            "max_order": 100000,
            "delivery_time": "1-6 jam"
        },
        "youtube_subscribers": {
            "name": "👥 Subscriber YouTube",
            "description": "Dapatkan subscriber YouTube berkualitas tinggi",
            "features": [
                "✅ Subscriber real & aktif",
                "✅ Profile lengkap dengan foto",
                "✅ Tidak akan unsubscribe",
                "✅ Aman dari algoritma YouTube",
                "✅ Garansi lifetime"
            ],
            "pricing": "1 token = 1 subscriber",
            "min_order": 10,
            "max_order": 50000,
            "delivery_time": "1-12 jam"
        },
        "instagram_likes": {
            "name": "❤️ Likes Instagram",
            "description": "Boost likes postingan Instagram Anda",
            "features": [
                "✅ Likes dari akun real",
                "✅ Profile foto & bio lengkap",
                "✅ Delivery cepat & aman",
                "✅ Tidak akan berkurang",
                "✅ Garansi refill 60 hari"
            ],
            "pricing": "1 token = 10 likes",
            "min_order": 10,
            "max_order": 100000,
            "delivery_time": "5-30 menit"
        },
        "instagram_followers": {
            "name": "👥 Followers Instagram",
            "description": "Tambah followers Instagram berkualitas",
            "features": [
                "✅ Followers real & aktif",
                "✅ Profile lengkap dengan postingan",
                "✅ Engagement rate tinggi",
                "✅ Aman dari shadowban",
                "✅ Garansi 90 hari"
            ],
            "pricing": "1 token = 1 follower",
            "min_order": 10,
            "max_order": 25000,
            "delivery_time": "1-6 jam"
        },
        "tiktok_views": {
            "name": "👀 Views TikTok",
            "description": "Tingkatkan views video TikTok Anda",
            "features": [
                "✅ Views dari user real",
                "✅ Retention rate 90%+",
                "✅ Boost algoritma TikTok",
                "✅ Delivery super cepat",
                "✅ Garansi refill 30 hari"
            ],
            "pricing": "1 token = 100 views",
            "min_order": 100,
            "max_order": 1000000,
            "delivery_time": "1-30 menit"
        },
        "tiktok_likes": {
            "name": "❤️ Likes TikTok",
            "description": "Dapatkan likes TikTok dari user aktif",
            "features": [
                "✅ Likes dari akun verified",
                "✅ Profile lengkap & aktif",
                "✅ Boost engagement rate",
                "✅ Aman untuk FYP",
                "✅ Garansi refill 45 hari"
            ],
            "pricing": "1 token = 5 likes",
            "min_order": 10,
            "max_order": 50000,
            "delivery_time": "5-60 menit"
        }
    }
    
    return services.get(service_type, {
        "name": "Layanan Tidak Ditemukan",
        "description": "Layanan yang Anda cari tidak tersedia",
        "features": [],
        "pricing": "N/A",
        "min_order": 0,
        "max_order": 0,
        "delivery_time": "N/A"
    })

def format_service_message(service_type: str) -> str:
    """Format service information message"""
    service = get_service_description(service_type)
    
    features_text = "\n".join(service["features"])
    
    return f"""
🎯 **{service['name']}**

📝 **Deskripsi:**
{service['description']}

✨ **Fitur:**
{features_text}

💰 **Harga:** {service['pricing']}
📦 **Min Order:** {service['min_order']:,}
📦 **Max Order:** {service['max_order']:,}
⏱️ **Waktu Proses:** {service['delivery_time']}

Masukkan link dan jumlah yang diinginkan untuk melanjutkan!

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_order_summary_message(order_data: Dict[str, Any]) -> str:
    """Get order summary message"""
    service = get_service_description(order_data['service_type'])
    
    return f"""
📋 **Ringkasan Pesanan**

🎯 **Layanan:** {service['name']}
🔗 **Link:** {order_data['url']}
📊 **Jumlah:** {order_data['quantity']:,}
💰 **Biaya:** {order_data['cost']} token

⏱️ **Estimasi Selesai:** {order_data.get('estimated_time', 'N/A')}

Konfirmasi pesanan Anda di bawah ini.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_profile_message(user_data: Dict[str, Any]) -> str:
    """Get user profile message"""
    return f"""
👤 **Profil Pengguna**

📝 **Nama:** {user_data.get('first_name', 'N/A')} {user_data.get('last_name', '')}
🆔 **Username:** @{user_data.get('username', 'N/A')}
📱 **Telegram ID:** {user_data.get('telegram_id')}

💰 **Token Saldo:** {user_data.get('tokens', 0):,} token
💎 **Status:** {'Premium' if user_data.get('is_premium') else 'Gratis'}
📅 **Bergabung:** {user_data.get('registration_date', 'N/A')}
🕐 **Terakhir Aktif:** {user_data.get('last_active', 'N/A')}

📊 **Statistik:**
• Total Token Earned: {user_data.get('total_earned_tokens', 0):,}
• Total Token Spent: {user_data.get('total_spent_tokens', 0):,}
• Total Orders: {user_data.get('total_orders', 0):,}

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_token_info_message(user_data: Dict[str, Any]) -> str:
    """Get token information message"""
    return f"""
💰 **Informasi Token**

💎 **Saldo Saat Ini:** {user_data.get('tokens', 0):,} token

📊 **Riwayat Token:**
• Total Earned: {user_data.get('total_earned_tokens', 0):,} token
• Total Spent: {user_data.get('total_spent_tokens', 0):,} token
• Registration Bonus: 50 token

🎁 **Cara Mendapatkan Token:**
• Tonton iklan (5 token/iklan)
• Tugas harian (10-50 token)
• Referral bonus (25 token/referral)
• Upgrade premium (bonus 500 token)

💡 **Tips:**
- Tonton iklan setiap hari untuk token gratis
- Ajak teman untuk bonus referral
- Upgrade premium untuk benefit lebih

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_help_message() -> str:
    """Get help message"""
    return f"""
❓ **Bantuan Jam Tayang Pro**

🚀 **Cara Menggunakan:**
1️⃣ Pilih platform sosial media
2️⃣ Pilih jenis layanan
3️⃣ Masukkan link konten
4️⃣ Tentukan jumlah yang diinginkan
5️⃣ Konfirmasi dan tunggu prosesnya

💰 **Tentang Token:**
• 1 token = berbeda untuk setiap layanan
• Dapatkan 50 token gratis saat daftar
• Tonton iklan untuk token tambahan
• Token tidak akan expired

🎯 **Layanan Tersedia:**
• YouTube: Jam tayang, subscriber, likes, views
• Instagram: Likes, followers, views, comments
• TikTok: Views, likes, followers, shares
• Facebook: Likes, followers, shares, views

⚡ **Fitur Unggulan:**
• Proses otomatis 24/7
• Hasil terlihat natural
• Aman dari algoritma platform
• Garansi refill/replacement
• Support 24/7

📞 **Butuh Bantuan?**
Hubungi support kami atau kunjungi website.

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_ad_watch_message(ad_data: Dict[str, Any]) -> str:
    """Get advertisement watch message"""
    return f"""
📺 **Tonton Iklan untuk Token Gratis**

🎁 **Reward:** {ad_data.get('reward', 5)} token
⏱️ **Durasi Minimum:** {ad_data.get('duration', 30)} detik
📊 **Iklan Hari Ini:** {ad_data.get('watched_today', 0)}/{ad_data.get('daily_limit', 20)}

📝 **Cara Menonton:**
1️⃣ Klik tombol "Tonton Iklan"
2️⃣ Tunggu hingga iklan selesai
3️⃣ Klik "Selesai Menonton"
4️⃣ Token otomatis masuk ke akun

⚠️ **Penting:**
• Jangan skip iklan sebelum waktunya
• Pastikan koneksi internet stabil
• Satu iklan hanya bisa ditonton sekali

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_order_status_message(order_data: Dict[str, Any]) -> str:
    """Get order status message"""
    status_emoji = {
        'pending': '⏳',
        'processing': '🔄',
        'completed': '✅',
        'failed': '❌',
        'cancelled': '🚫'
    }
    
    status_text = {
        'pending': 'Menunggu Proses',
        'processing': 'Sedang Diproses',
        'completed': 'Selesai',
        'failed': 'Gagal',
        'cancelled': 'Dibatalkan'
    }
    
    status = order_data.get('status', 'pending')
    
    return f"""
📋 **Status Pesanan #{order_data.get('id')}**

{status_emoji.get(status, '❓')} **Status:** {status_text.get(status, 'Unknown')}
🎯 **Layanan:** {order_data.get('service_name')}
🔗 **Link:** {order_data.get('url')}
📊 **Progress:** {order_data.get('completed_quantity', 0):,}/{order_data.get('quantity', 0):,} ({order_data.get('progress_percentage', 0):.1f}%)

📅 **Dibuat:** {order_data.get('created_at', 'N/A')}
⏱️ **Estimasi Selesai:** {order_data.get('estimated_completion', 'N/A')}

{f"❌ **Error:** {order_data.get('error_message')}" if order_data.get('error_message') else ""}

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_admin_stats_message(stats: Dict[str, Any]) -> str:
    """Get admin statistics message"""
    return f"""
📊 **Statistik Admin Panel**

👥 **Users:**
• Total Users: {stats.get('total_users', 0):,}
• Active Today: {stats.get('active_today', 0):,}
• New Today: {stats.get('new_today', 0):,}
• Premium Users: {stats.get('premium_users', 0):,}

📋 **Orders:**
• Total Orders: {stats.get('total_orders', 0):,}
• Pending: {stats.get('pending_orders', 0):,}
• Processing: {stats.get('processing_orders', 0):,}
• Completed Today: {stats.get('completed_today', 0):,}

💰 **Tokens:**
• Total Distributed: {stats.get('total_tokens_distributed', 0):,}
• Spent Today: {stats.get('tokens_spent_today', 0):,}
• Earned Today: {stats.get('tokens_earned_today', 0):,}

📺 **Ads:**
• Views Today: {stats.get('ad_views_today', 0):,}
• Tokens from Ads: {stats.get('tokens_from_ads', 0):,}

🖥️ **System:**
• Uptime: {stats.get('uptime', 'N/A')}
• Memory Usage: {stats.get('memory_usage', 'N/A')}
• Active Tasks: {stats.get('active_tasks', 0):,}

---
*By Kantong Aplikasi 2025*
*https://www.kantongaplikasi.com/*
    """

def get_error_message(error_type: str) -> str:
    """Get error message based on type"""
    errors = {
        'insufficient_tokens': '❌ Token Anda tidak mencukupi untuk layanan ini.',
        'invalid_url': '❌ Link yang Anda masukkan tidak valid.',
        'service_unavailable': '❌ Layanan sedang tidak tersedia. Coba lagi nanti.',
        'rate_limit': '❌ Anda telah mencapai batas maksimal. Coba lagi nanti.',
        'maintenance': '🔧 Sistem sedang dalam maintenance. Mohon tunggu.',
        'banned_user': '🚫 Akun Anda telah diblokir. Hubungi admin.',
        'invalid_quantity': '❌ Jumlah yang Anda masukkan tidak valid.',
        'order_failed': '❌ Pesanan gagal diproses. Token akan dikembalikan.',
        'network_error': '❌ Terjadi kesalahan jaringan. Silakan coba lagi.',
        'unknown_error': '❌ Terjadi kesalahan tidak dikenal. Hubungi support.'
    }
    
    return errors.get(error_type, errors['unknown_error'])

def get_success_message(action: str, details: str = "") -> str:
    """Get success message"""
    messages = {
        'order_created': f'✅ Pesanan berhasil dibuat! {details}',
        'tokens_added': f'✅ Token berhasil ditambahkan! {details}',
        'profile_updated': f'✅ Profil berhasil diperbarui! {details}',
        'ad_completed': f'✅ Iklan selesai ditonton! {details}',
        'order_completed': f'✅ Pesanan selesai diproses! {details}',
        'registration': f'✅ Registrasi berhasil! {details}',
        'settings_updated': f'✅ Pengaturan berhasil diperbarui! {details}'
    }
    
    return messages.get(action, f'✅ Berhasil! {details}')
