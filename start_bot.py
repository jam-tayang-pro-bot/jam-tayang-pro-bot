#!/usr/bin/env python3
"""
Quick start script for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking requirements...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required!")
        return False
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Run: python install.py first")
        return False
    
    # Check if dependencies are installed
    try:
        import telegram
        import sqlalchemy
        import aiohttp
        print("✅ Dependencies OK")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main function to start the bot"""
    print("🚀 Starting Jam Tayang Pro Bot...")
    print("By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/")
    print("-" * 60)
    
    if not check_requirements():
        print("\n❌ Requirements not met. Please fix the issues above.")
        input("Press Enter to exit...")
        return
    
    # Start the main bot
    try:
        from main import main as bot_main
        import asyncio
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting bot: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
