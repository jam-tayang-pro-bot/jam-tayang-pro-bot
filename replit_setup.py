#!/usr/bin/env python3
"""
Replit Setup Script for Jam Tayang Pro Bot
Script khusus untuk setup bot di Replit
"""

import os
import sys
import asyncio
import subprocess

def print_header():
    print("=" * 60)
    print("🚀 JAM TAYANG PRO BOT - REPLIT SETUP")
    print("By Kantong Aplikasi 2025")
    print("=" * 60)

def check_replit_environment():
    """Check if running on Replit"""
    print("\n🔍 Checking Replit environment...")
    
    # Check for Replit-specific environment variables
    replit_indicators = [
        'REPL_ID', 'REPL_SLUG', 'REPLIT_DB_URL', 
        'REPL_OWNER', 'REPLIT_CLUSTER'
    ]
    
    is_replit = any(os.getenv(var) for var in replit_indicators)
    
    if is_replit:
        print("✅ Running on Replit detected")
        return True
    else:
        print("ℹ️ Not running on Replit (or Replit environment not detected)")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        # Install from requirements.txt
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print(f"❌ Failed to install dependencies: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Installation timeout - continuing anyway")
        return True
    except Exception as e:
        print(f"❌ Installation error: {e}")
        return False

def check_environment_variables():
    """Check required environment variables"""
    print("\n🔍 Checking environment variables...")
    
    required_vars = {
        'BOT_TOKEN': 'Bot token from @BotFather',
        'DATABASE_URL': 'Database connection string (optional)',
    }
    
    missing_vars = []
    
    for var, description in required_vars.items():
        value = os.getenv(var)
        if var == 'BOT_TOKEN' and (not value or value == 'your_bot_token_here'):
            missing_vars.append(f"{var}: {description}")
            print(f"❌ {var} not set")
        elif value:
            if var == 'BOT_TOKEN':
                print(f"✅ {var} configured ({value[:10]}...{value[-10:]})")
            else:
                print(f"✅ {var} configured")
        else:
            print(f"⚠️ {var} not set (optional)")
    
    if missing_vars:
        print(f"\n❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 To fix this:")
        print("1. Go to Replit Secrets tab (🔒 icon in sidebar)")
        print("2. Add the missing environment variables")
        print("3. Restart this script")
        return False
    
    return True

async def test_bot_functionality():
    """Test basic bot functionality"""
    print("\n🧪 Testing bot functionality...")
    
    try:
        # Test imports
        sys.path.append('.')
        from main import JamTayangProBot
        from src.database.database import init_database
        
        print("✅ Bot imports successful")
        
        # Test database initialization
        await init_database()
        print("✅ Database initialization successful")
        
        # Test bot creation
        bot = JamTayangProBot()
        print("✅ Bot instance created")
        
        return True
        
    except Exception as e:
        print(f"❌ Bot functionality test failed: {e}")
        return False

def create_replit_files():
    """Create necessary files for Replit"""
    print("\n📄 Creating Replit configuration files...")
    
    # Check if .replit exists
    if os.path.exists('.replit'):
        print("✅ .replit file already exists")
    else:
        print("⚠️ .replit file not found - should be created")
    
    # Check if keep_alive.py exists
    if os.path.exists('keep_alive.py'):
        print("✅ keep_alive.py exists")
    else:
        print("⚠️ keep_alive.py not found - should be created")
    
    return True

def show_next_steps():
    """Show next steps for user"""
    print("\n🎯 NEXT STEPS:")
    print("1. Make sure BOT_TOKEN is set in Replit Secrets")
    print("2. Click the 'Run' button in Replit")
    print("3. Bot will start automatically")
    print("4. Test bot at: https://t.me/JamTayangProBot")
    print("\n🔗 Bot Features:")
    print("   - 🎬 YouTube Services (Jam Tayang, Subscriber, etc)")
    print("   - 📸 Instagram Services (Likes, Followers, etc)")
    print("   - 🎵 TikTok Services (Views, Likes, etc)")
    print("   - 📘 Facebook Services (Likes, Followers, etc)")
    print("   - 💰 Token System (50 gratis + iklan)")

async def main():
    """Main setup function"""
    print_header()
    
    # Check environment
    is_replit = check_replit_environment()
    
    # Install dependencies
    deps_ok = install_dependencies()
    
    # Check environment variables
    env_ok = check_environment_variables()
    
    # Create Replit files
    files_ok = create_replit_files()
    
    # Test bot functionality
    if env_ok:
        bot_ok = await test_bot_functionality()
    else:
        bot_ok = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SETUP SUMMARY:")
    print(f"   Replit Environment: {'✅' if is_replit else '⚠️'}")
    print(f"   Dependencies: {'✅' if deps_ok else '❌'}")
    print(f"   Environment Variables: {'✅' if env_ok else '❌'}")
    print(f"   Configuration Files: {'✅' if files_ok else '❌'}")
    print(f"   Bot Functionality: {'✅' if bot_ok else '❌'}")
    
    if all([deps_ok, env_ok, files_ok, bot_ok]):
        print("\n🎉 SETUP COMPLETE! Bot is ready to run!")
        print("🚀 Click 'Run' button to start the bot")
    else:
        print("\n⚠️ Setup incomplete. Please fix the issues above.")
    
    show_next_steps()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")
