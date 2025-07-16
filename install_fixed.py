#!/usr/bin/env python3
"""
Installation script for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print installation banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    JAM TAYANG PRO BOT                        ║
║              Professional Social Media Bot                   ║
║                                                              ║
║           By Kantong Aplikasi 2025                          ║
║           https://www.kantongaplikasi.com/                  ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 atau lebih baru diperlukan!")
        print(f"Versi Python Anda: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} - OK")

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    except FileNotFoundError:
        print("❌ requirements.txt not found!")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        "logs",
        "data", 
        "temp",
        "backups"
    ]
    
    for directory in directories:
        try:
            Path(directory).mkdir(exist_ok=True)
            print(f"✅ Created directory: {directory}")
        except Exception as e:
            print(f"⚠️  Could not create directory {directory}: {e}")

def setup_environment():
    """Setup environment file"""
    print("\n⚙️ Setting up environment...")
    
    if not os.path.exists('.env'):
        env_template = """# Telegram Bot Configuration
BOT_TOKEN=your_telegram_bot_token_here

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
        
        try:
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(env_template)
            print("✅ Created .env file from template")
            print("⚠️  IMPORTANT: Edit .env file and add your BOT_TOKEN!")
        except Exception as e:
            print(f"❌ Could not create .env file: {e}")
    else:
        print("✅ .env file already exists")

def create_startup_scripts():
    """Create startup scripts"""
    print("\n🚀 Creating startup scripts...")
    
    try:
        # Windows batch file
        windows_script = """@echo off
echo Starting Jam Tayang Pro Bot...
python main.py
pause
"""
        
        with open('start_bot.bat', 'w') as f:
            f.write(windows_script)
        
        # Linux/Mac shell script
        linux_script = """#!/bin/bash
echo "Starting Jam Tayang Pro Bot..."
python3 main.py
"""
        
        with open('start_bot.sh', 'w') as f:
            f.write(linux_script)
        
        # Make shell script executable on Unix systems
        if os.name != 'nt':
            try:
                os.chmod('start_bot.sh', 0o755)
            except:
                pass
        
        print("✅ Created startup scripts")
    except Exception as e:
        print(f"⚠️  Could not create startup scripts: {e}")

def check_bot_token():
    """Check if bot token is configured"""
    print("\n🔑 Checking bot token...")
    
    try:
        if os.path.exists('.env'):
            with open('.env', 'r', encoding='utf-8') as f:
                content = f.read()
                if 'BOT_TOKEN=' in content and 'your_telegram_bot_token_here' not in content:
                    print("✅ Bot token appears to be configured")
                    return True
                else:
                    print("⚠️  BOT_TOKEN not configured!")
                    print("Please edit .env file and add your Telegram bot token")
                    return False
        else:
            print("⚠️  .env file not found")
            return False
    except Exception as e:
        print(f"⚠️  Could not check bot token: {e}")
        return False

def test_imports():
    """Test if main modules can be imported"""
    print("\n🧪 Testing imports...")
    
    try:
        sys.path.insert(0, '.')
        import src
        print("✅ Main package imported successfully")
        return True
    except Exception as e:
        print(f"⚠️  Import test failed: {e}")
        print("This is normal if dependencies aren't installed yet")
        return False

def print_next_steps():
    """Print next steps for user"""
    print("\n" + "="*60)
    print("🎉 INSTALLATION COMPLETED!")
    print("="*60)
    
    print("\n📋 NEXT STEPS:")
    print("1. Edit .env file and configure your settings:")
    print("   - BOT_TOKEN: Your Telegram bot token")
    print("   - ADMIN_USER_IDS: Your Telegram user ID")
    
    print("\n2. Get your Telegram ID:")
    print("   - Chat with @userinfobot in Telegram")
    print("   - Copy the ID to ADMIN_USER_IDS in .env")
    
    print("\n3. Start the bot:")
    if os.name == 'nt':
        print("   - Double-click start_bot.bat")
        print("   - Or run: python main.py")
    else:
        print("   - Run: ./start_bot.sh")
        print("   - Or run: python3 main.py")
    
    print("\n4. Test your bot:")
    print("   - Go to: https://t.me/JamTayangProBot")
    print("   - Send /start to your bot")
    print("   - Test registration with /daftar")
    
    print("\n📞 SUPPORT:")
    print("   - Website: https://www.kantongaplikasi.com/")
    print("   - Documentation: README.md, PANDUAN_INSTALASI.md")
    
    print("\n" + "="*60)

def main():
    """Main installation function"""
    print_banner()
    
    print("🔧 Starting installation process...\n")
    
    try:
        # Check Python version
        check_python_version()
        
        # Install requirements
        deps_ok = install_requirements()
        
        # Create directories
        create_directories()
        
        # Setup environment
        setup_environment()
        
        # Create startup scripts
        create_startup_scripts()
        
        # Check bot token
        token_configured = check_bot_token()
        
        # Test imports
        imports_ok = test_imports()
        
        # Print results
        print("\n" + "="*60)
        print("📊 INSTALLATION SUMMARY:")
        print("="*60)
        print(f"✅ Python version: OK")
        print(f"{'✅' if deps_ok else '❌'} Dependencies: {'Installed' if deps_ok else 'Failed'}")
        print(f"✅ Directories: Created")
        print(f"✅ Environment: Setup")
        print(f"✅ Scripts: Created")
        print(f"{'✅' if token_configured else '⚠️ '} Bot token: {'Configured' if token_configured else 'Needs configuration'}")
        print(f"{'✅' if imports_ok else '⚠️ '} Imports: {'OK' if imports_ok else 'Needs testing after deps'}")
        
        if deps_ok and token_configured:
            print("\n🎉 Installation completed successfully!")
            print("Your bot is ready to run!")
        else:
            print("\n⚠️  Installation completed with warnings.")
            if not deps_ok:
                print("Please fix dependency installation issues.")
            if not token_configured:
                print("Please configure your bot token before running.")
        
        print_next_steps()
        
    except Exception as e:
        print(f"\n❌ Installation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
