#!/usr/bin/env python3
"""
Setup script untuk konfigurasi Bot Telegram "Jam Tayang Pro"
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
import sys

def setup_bot_token():
    """Setup bot token dan konfigurasi dasar"""
    print("🤖 Setup Bot Telegram 'Jam Tayang Pro'")
    print("=" * 50)
    
    # Bot token dari BotFather
    bot_token = "8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90"
    
    # Buat file .env
    env_content = f"""# Telegram Bot Configuration
BOT_TOKEN={bot_token}

# Admin Configuration (Ganti dengan Telegram ID Anda)
ADMIN_USER_IDS=123456789

# Database Configuration
DATABASE_URL=sqlite:///jam_tayang_pro.db

# Security Configuration
SECRET_KEY=jam_tayang_pro_secret_key_2025
ENCRYPTION_KEY=your_encryption_key_here

# Rate Limiting
MAX_REQUESTS_PER_MINUTE=30
MAX_ORDERS_PER_DAY=50

# Token System
WELCOME_BONUS_TOKENS=50
AD_REWARD_TOKENS=5
DAILY_AD_LIMIT=20
REFERRAL_BONUS_TOKENS=25

# Service Pricing (dalam token)
YOUTUBE_WATCHTIME_RATE=1
INSTAGRAM_LIKES_RATE=1
TIKTOK_VIEWS_RATE=1
FACEBOOK_LIKES_RATE=1

# Automation Settings
MIN_DELAY_SECONDS=30
MAX_DELAY_SECONDS=300
HUMAN_BEHAVIOR_ENABLED=true

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/bot.log

# Development
DEBUG=false
WEBHOOK_URL=
WEBHOOK_PORT=8443
"""
    
    # Tulis file .env
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ File .env berhasil dibuat!")
    print(f"✅ Bot Token: {bot_token[:20]}...")
    print("✅ Bot URL: https://t.me/JamTayangProBot")
    
    print("\n📝 PENTING - Edit file .env:")
    print("1. Ganti ADMIN_USER_IDS dengan Telegram ID Anda")
    print("2. Sesuaikan konfigurasi lainnya jika diperlukan")
    
    return True

def get_telegram_id_instructions():
    """Instruksi untuk mendapatkan Telegram ID"""
    print("\n🆔 Cara Mendapatkan Telegram ID Anda:")
    print("1. Chat dengan @userinfobot di Telegram")
    print("2. Bot akan memberikan ID Anda")
    print("3. Copy ID tersebut ke ADMIN_USER_IDS di file .env")
    print("4. Contoh: ADMIN_USER_IDS=123456789,987654321")

def setup_directories():
    """Buat direktori yang diperlukan"""
    directories = ['logs', 'data', 'temp', 'backups']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Direktori {directory} dibuat")

def main():
    """Main setup function"""
    print("🚀 Memulai setup Bot 'Jam Tayang Pro'...")
    
    try:
        # Setup directories
        setup_directories()
        
        # Setup bot token
        setup_bot_token()
        
        # Instructions
        get_telegram_id_instructions()
        
        print("\n🎉 Setup berhasil!")
        print("\n📋 Langkah selanjutnya:")
        print("1. Edit file .env dengan Telegram ID Anda")
        print("2. Jalankan: python main.py")
        print("3. Test bot di: https://t.me/JamTayangProBot")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        return False

if __name__ == "__main__":
    main()
