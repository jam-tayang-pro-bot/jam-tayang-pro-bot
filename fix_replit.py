#!/usr/bin/env python3
"""
Script sederhana untuk fix masalah di Replit
Jam Tayang Pro Bot - By Kantong Aplikasi 2025
"""

import subprocess
import sys

def main():
    print("🔧 Fixing Replit Dependencies...")
    
    # Install essential packages
    packages = [
        "python-telegram-bot==20.7",
        "python-dotenv==1.0.0"
    ]
    
    for package in packages:
        print(f"📦 Installing {package}...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
    
    # Test imports
    print("\n🧪 Testing imports...")
    try:
        import telegram
        print("✅ telegram imported successfully")
    except ImportError:
        print("❌ telegram import failed")
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError:
        print("❌ python-dotenv import failed")
    
    print("\n📋 NEXT STEPS:")
    print("1. Add BOT_TOKEN to Secrets")
    print("2. Add ADMIN_USER_IDS to Secrets")
    print("3. Click Run button")
    print("\n✅ Fix completed!")

if __name__ == "__main__":
    main()
