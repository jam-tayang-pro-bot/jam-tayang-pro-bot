#!/usr/bin/env python3
"""
Installation script for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
import sys
import subprocess
import shutil
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
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    
    return True

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
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def setup_environment():
    """Setup environment file"""
    print("\n⚙️ Setting up environment...")
    
    if not os.path.exists('.env'):
        shutil.copy('.env.example', '.env')
        print("✅ Created .env file from template")
        print("⚠️  IMPORTANT: Edit .env file and add your BOT_TOKEN!")
    else:
        print("✅ .env file already exists")

def create_startup_scripts():
    """Create startup scripts"""
    print("\n🚀 Creating startup scripts...")
    
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
        os.chmod('start_bot.sh', 0o755)
    
    print("✅ Created startup scripts")

def check_bot_token():
    """Check if bot token is configured"""
    print("\n🔑 Checking bot token...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        bot_token = os.getenv('BOT_TOKEN')
        if not bot_token or bot_token == 'your_telegram_bot_token_here':
            print("⚠️  BOT_TOKEN not configured!")
            print("Please edit .env file and add your Telegram bot token")
            return False
        else:
            print("✅ Bot token configured")
            return True
    except ImportError:
        print("⚠️  Could not check bot token (python-dotenv not installed)")
        return False

def test_database():
    """Test database connection"""
    print("\n🗄️ Testing database...")
    
    try:
        import asyncio
        from src.database.database import init_database
        
        async def test_db():
            await init_database()
            print("✅ Database initialized successfully")
        
        asyncio.run(test_db())
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
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
    print("   - Other optional settings")
    
    print("\n2. Start the bot:")
    if os.name == 'nt':
        print("   - Double-click start_bot.bat")
        print("   - Or run: python main.py")
    else:
        print("   - Run: ./start_bot.sh")
        print("   - Or run: python3 main.py")
    
    print("\n3. Test your bot:")
    print("   - Send /start to your bot in Telegram")
    print("   - Check if registration works")
    print("   - Test basic commands")
    
    print("\n📞 SUPPORT:")
    print("   - Website: https://www.kantongaplikasi.com/")
    print("   - Email: support@kantongaplikasi.com")
    print("   - Telegram: @kantongaplikasi")
    
    print("\n" + "="*60)

def main():
    """Main installation function"""
    print_banner()
    
    print("🔧 Starting installation process...\n")
    
    # Check Python version
    check_python_version()
    
    # Install requirements
    if not install_requirements():
        print("❌ Installation failed!")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Setup environment
    setup_environment()
    
    # Create startup scripts
    create_startup_scripts()
    
    # Check bot token
    token_configured = check_bot_token()
    
    # Test database
    db_ok = test_database()
    
    # Print results
    print("\n" + "="*60)
    print("📊 INSTALLATION SUMMARY:")
    print("="*60)
    print(f"✅ Python version: OK")
    print(f"✅ Dependencies: Installed")
    print(f"✅ Directories: Created")
    print(f"✅ Environment: Setup")
    print(f"✅ Scripts: Created")
    print(f"{'✅' if token_configured else '⚠️ '} Bot token: {'Configured' if token_configured else 'Needs configuration'}")
    print(f"{'✅' if db_ok else '❌'} Database: {'OK' if db_ok else 'Error'}")
    
    if token_configured and db_ok:
        print("\n🎉 Installation completed successfully!")
        print("Your bot is ready to run!")
    else:
        print("\n⚠️  Installation completed with warnings.")
        print("Please fix the issues above before running the bot.")
    
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Installation failed: {e}")
        sys.exit(1)
