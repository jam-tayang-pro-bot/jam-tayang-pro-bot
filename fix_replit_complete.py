#!/usr/bin/env python3
"""
Script lengkap untuk fix masalah di Replit
Jam Tayang Pro Bot - By Kantong Aplikasi 2025
"""

import subprocess
import sys
import os

def main():
    print("🔧 FIXING REPLIT ISSUES - COMPLETE SOLUTION")
    print("=" * 60)
    
    # Step 1: Install dependencies
    print("\n📦 Step 1: Installing dependencies...")
    packages = [
        "python-telegram-bot==20.7",
        "python-dotenv==1.0.0",
        "sqlalchemy==2.0.23",
        "aiohttp==3.9.1"
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], 
                         check=True, capture_output=True)
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
    
    # Step 2: Add current directory to Python path
    print("\n🔧 Step 2: Adding project to Python path...")
    current_dir = os.getcwd()
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
        print(f"✅ Added {current_dir} to Python path")
    
    # Step 3: Test imports
    print("\n🧪 Step 3: Testing imports...")
    
    # Test telegram
    try:
        import telegram
        print("✅ telegram imported successfully")
    except ImportError as e:
        print(f"❌ telegram import failed: {e}")
    
    # Test dotenv
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
    
    # Test src modules
    try:
        from src.bot.handlers import start_handler
        print("✅ src.bot.handlers imported successfully")
    except ImportError as e:
        print(f"❌ src.bot.handlers import failed: {e}")
        print("   This is normal if __init__.py files are missing")
    
    # Step 4: Create missing directories if needed
    print("\n📁 Step 4: Checking directory structure...")
    dirs_to_check = [
        "logs", "data", "temp", "backups"
    ]
    
    for dir_name in dirs_to_check:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"✅ Created directory: {dir_name}")
        else:
            print(f"✅ Directory exists: {dir_name}")
    
    print("\n" + "=" * 60)
    print("🎉 REPLIT FIX COMPLETED!")
    print("=" * 60)
    
    print("\n📋 NEXT STEPS:")
    print("1. Add BOT_TOKEN to Replit Secrets")
    print("2. Add ADMIN_USER_IDS to Replit Secrets")
    print("3. Click the Run button")
    
    print("\n🔗 GET BOT TOKEN:")
    print("1. Chat with @BotFather on Telegram")
    print("2. Send /newbot and follow instructions")
    print("3. Copy the token to Replit Secrets")
    
    print("\n🆔 GET USER ID:")
    print("1. Chat with @userinfobot on Telegram")
    print("2. Copy your User ID to Replit Secrets")
    
    print("\n✅ Bot siap dijalankan!")

if __name__ == "__main__":
    main()
