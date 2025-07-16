#!/usr/bin/env python3
"""
Setup script khusus untuk Replit.com
Jam Tayang Pro Bot - By Kantong Aplikasi 2025
"""

import subprocess
import sys
import os

def print_banner():
    """Print setup banner"""
    print("=" * 60)
    print("JAM TAYANG PRO BOT - REPLIT SETUP")
    print("By Kantong Aplikasi 2025")
    print("https://www.kantongaplikasi.com/")
    print("=" * 60)

def install_dependencies():
    """Install required dependencies for Replit"""
    print("\n🔧 Installing dependencies for Replit...")
    
    # Install from requirements.txt first
    try:
        print("📦 Installing from requirements.txt...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"
        ])
        print("✅ Requirements.txt installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Could not install from requirements.txt: {e}")
        
        # Fallback: install essential packages manually
        essential_packages = [
            "python-telegram-bot==20.7",
            "python-dotenv==1.0.0",
            "sqlalchemy==2.0.23",
            "aiohttp==3.9.1",
            "requests==2.31.0"
        ]
        
        print("📦 Installing essential packages manually...")
        for package in essential_packages:
            try:
                print(f"Installing {package}...")
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", package, "--quiet"
                ])
                print(f"✅ {package} installed")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                continue
    
    print("✅ Dependencies installation completed!")

def check_environment():
    """Check if running in Replit environment"""
    replit_indicators = ['REPL_ID', 'REPL_SLUG', 'REPLIT_DB_URL']
    is_replit = any(indicator in os.environ for indicator in replit_indicators)
    
    if is_replit:
        print("✅ Running in Replit environment")
        return True
    else:
        print("⚠️  Not detected as Replit environment (but continuing anyway)")
        return False

def test_imports():
    """Test if critical imports work"""
    print("\n🧪 Testing critical imports...")
    
    try:
        import telegram
        print("✅ telegram library imported successfully")
    except ImportError as e:
        print(f"❌ telegram import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    try:
        import sqlalchemy
        print("✅ sqlalchemy imported successfully")
    except ImportError as e:
        print(f"❌ sqlalchemy import failed: {e}")
        return False
    
    return True

def print_instructions():
    """Print setup instructions"""
    print("\n" + "=" * 60)
    print("🎉 REPLIT SETUP COMPLETED!")
    print("=" * 60)
    
    print("\n📋 LANGKAH SELANJUTNYA:")
    print("1. Klik tab 'Secrets' di Replit")
    print("2. Tambahkan secret baru:")
    print("   - Key: BOT_TOKEN")
    print("   - Value: Token bot Telegram Anda dari @BotFather")
    
    print("\n3. Tambahkan secret admin:")
    print("   - Key: ADMIN_USER_IDS") 
    print("   - Value: Telegram User ID Anda")
    
    print("\n4. Klik tombol 'Run' untuk menjalankan bot")
    
    print("\n🔗 CARA MENDAPATKAN BOT TOKEN:")
    print("1. Chat dengan @BotFather di Telegram")
    print("2. Kirim /newbot")
    print("3. Ikuti instruksi untuk membuat bot")
    print("4. Copy token yang diberikan")
    
    print("\n🆔 CARA MENDAPATKAN USER ID:")
    print("1. Chat dengan @userinfobot di Telegram")
    print("2. Copy User ID yang ditampilkan")
    
    print("\n" + "=" * 60)

def main():
    """Main setup function"""
    try:
        print_banner()
        
        # Check environment
        is_replit = check_environment()
        
        # Install dependencies
        install_dependencies()
        
        # Test imports
        imports_ok = test_imports()
        
        if imports_ok:
            print("\n✅ All critical imports working!")
        else:
            print("\n⚠️  Some imports failed. Try running:")
            print("pip install python-telegram-bot==20.7 python-dotenv")
        
        # Print instructions
        print_instructions()
        
        print("✅ Setup completed! Bot siap dijalankan di Replit.")
        
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        print("Try running manually:")
        print("pip install python-telegram-bot==20.7")
        print("pip install python-dotenv")

if __name__ == "__main__":
    main()
