#!/usr/bin/env python3
"""
Setup and Test Script for Jam Tayang Pro Bot
Membantu setup awal dan testing bot
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path

def print_header():
    print("=" * 60)
    print("🚀 JAM TAYANG PRO BOT - SETUP & TEST")
    print("By Kantong Aplikasi 2025")
    print("=" * 60)

def check_python_version():
    print("\n🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+")
        return False

def check_dependencies():
    print("\n🔍 Checking dependencies...")
    try:
        import telegram
        import sqlalchemy
        import aiohttp
        import aiosqlite
        print("✅ All dependencies installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def check_env_file():
    print("\n🔍 Checking .env configuration...")
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        print("📝 Creating .env from template...")
        
        if os.path.exists('.env.example'):
            # Copy .env.example to .env
            with open('.env.example', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("✅ .env file created from template")
            print("⚠️  Please edit .env and set your BOT_TOKEN")
            return False
        else:
            print("❌ .env.example not found")
            return False
    
    # Check BOT_TOKEN
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token or bot_token == 'your_bot_token_here':
        print("❌ BOT_TOKEN not set in .env")
        print("📝 Please get token from @BotFather and set in .env")
        return False
    
    print("✅ .env file configured")
    return True

async def test_database():
    print("\n🔍 Testing database operations...")
    try:
        sys.path.append('.')
        from src.database.database import init_database, create_user, get_user_by_telegram_id
        
        await init_database()
        print("✅ Database initialized")
        
        # Test user creation
        test_user = await create_user(
            telegram_id='999999999',
            username='test_setup',
            first_name='Test',
            last_name='Setup'
        )
        print("✅ User creation works")
        
        # Test user retrieval
        retrieved_user = await get_user_by_telegram_id('999999999')
        if retrieved_user:
            print("✅ User retrieval works")
        
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_bot_import():
    print("\n🔍 Testing bot imports...")
    try:
        sys.path.append('.')
        from main import JamTayangProBot
        bot = JamTayangProBot()
        print("✅ Bot class import successful")
        return True
    except Exception as e:
        print(f"❌ Bot import failed: {e}")
        return False

async def run_tests():
    print("\n🧪 Running comprehensive tests...")
    
    tests_passed = 0
    total_tests = 5
    
    # Test 1: Python version
    if check_python_version():
        tests_passed += 1
    
    # Test 2: Dependencies
    if check_dependencies():
        tests_passed += 1
    
    # Test 3: Environment
    if check_env_file():
        tests_passed += 1
    
    # Test 4: Database
    if await test_database():
        tests_passed += 1
    
    # Test 5: Bot import
    if test_bot_import():
        tests_passed += 1
    
    print(f"\n📊 Test Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Bot is ready to run!")
        print("\n🚀 To start the bot, run:")
        print("   python main.py")
        return True
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        return False

def install_dependencies():
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def main():
    print_header()
    
    print("\n🔧 SETUP OPTIONS:")
    print("1. Run full setup and test")
    print("2. Install dependencies only")
    print("3. Run tests only")
    print("4. Create .env file")
    print("5. Exit")
    
    try:
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            print("\n🚀 Running full setup...")
            install_dependencies()
            asyncio.run(run_tests())
            
        elif choice == "2":
            install_dependencies()
            
        elif choice == "3":
            asyncio.run(run_tests())
            
        elif choice == "4":
            check_env_file()
            
        elif choice == "5":
            print("👋 Goodbye!")
            
        else:
            print("❌ Invalid option")
            
    except KeyboardInterrupt:
        print("\n👋 Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")

if __name__ == "__main__":
    main()
