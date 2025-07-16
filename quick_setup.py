#!/usr/bin/env python3
"""
Quick Setup Script for Jam Tayang Pro Bot
"""

import os
import sys
import asyncio
from pathlib import Path

async def quick_setup():
    print("🚀 JAM TAYANG PRO BOT - QUICK SETUP")
    print("=" * 50)
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("📝 Creating .env file...")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("✅ .env file created from template")
        else:
            # Create basic .env
            with open('.env', 'w') as f:
                f.write("BOT_TOKEN=your_bot_token_here\n")
                f.write("DATABASE_URL=sqlite:///jam_tayang_pro.db\n")
                f.write("ADMIN_USER_IDS=\n")
            print("✅ Basic .env file created")
    
    # Test imports
    print("\n🔍 Testing imports...")
    try:
        sys.path.append('.')
        from src.database.database import init_database
        from main import JamTayangProBot
        print("✅ All imports successful")
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Test database
    print("\n🔍 Testing database...")
    try:
        await init_database()
        print("✅ Database initialization successful")
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    # Check BOT_TOKEN
    print("\n🔍 Checking BOT_TOKEN...")
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token or bot_token == 'your_bot_token_here':
        print("⚠️  BOT_TOKEN not set")
        print("\n📋 NEXT STEPS:")
        print("1. Get bot token from @BotFather on Telegram")
        print("2. Edit .env file and replace 'your_bot_token_here' with your token")
        print("3. Run: python main.py")
        return False
    else:
        print("✅ BOT_TOKEN is configured")
        print("\n🎉 Setup complete! Bot is ready to run!")
        print("🚀 Run: python main.py")
        return True

if __name__ == "__main__":
    asyncio.run(quick_setup())
