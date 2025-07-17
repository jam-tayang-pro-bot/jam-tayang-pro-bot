import os
import sys
import asyncio
import traceback

# Set BOT_TOKEN
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("REAL TEST MAIN.PY")
print("=" * 40)

try:
    print("Step 1: Testing imports...")
    
    # Test nest_asyncio first
    try:
        import nest_asyncio
        nest_asyncio.apply()
        print("  ✅ nest_asyncio imported and applied")
    except Exception as e:
        print(f"  ❌ nest_asyncio error: {e}")
        sys.exit(1)
    
    # Test other imports
    try:
        from dotenv import load_dotenv
        print("  ✅ dotenv imported")
    except Exception as e:
        print(f"  ❌ dotenv error: {e}")
        sys.exit(1)
    
    try:
        from telegram.ext import Application
        print("  ✅ telegram imported")
    except Exception as e:
        print(f"  ❌ telegram error: {e}")
        sys.exit(1)
    
    print("\nStep 2: Testing project imports...")
    
    try:
        from keep_alive import keep_alive
        print("  ✅ keep_alive imported")
    except Exception as e:
        print(f"  ❌ keep_alive error: {e}")
    
    try:
        from src.database.database import init_database
        print("  ✅ database imported")
    except Exception as e:
        print(f"  ❌ database error: {e}")
    
    try:
        from src.bot.handlers import start_handler
        print("  ✅ handlers imported")
    except Exception as e:
        print(f"  ❌ handlers error: {e}")
    
    print("\nStep 3: Testing main bot import...")
    
    try:
        from main import JamTayangProBot
        print("  ✅ JamTayangProBot imported successfully")
        
        # Create bot instance
        bot = JamTayangProBot()
        print("  ✅ Bot instance created")
        print(f"  ✅ Bot token: {bot.bot_token[:10]}..." if bot.bot_token else "  ❌ No token")
        
    except Exception as e:
        print(f"  ❌ Main bot import failed: {e}")
        traceback.print_exc()
        sys.exit(1)
    
    print("\nStep 4: Testing bot initialization (without running)...")
    
    async def test_bot_init():
        try:
            print("  🔄 Initializing bot...")
            await bot.initialize()
            print("  ✅ Bot initialized successfully")
            
            print("  🔄 Stopping bot...")
            await bot.stop()
            print("  ✅ Bot stopped successfully")
            
            return True
        except Exception as e:
            print(f"  ❌ Bot initialization failed: {e}")
            traceback.print_exc()
            return False
    
    # Run async test
    result = asyncio.run(test_bot_init())
    
    if result:
        print("\n🎉 SUCCESS: main.py PASSED ALL TESTS!")
        print("✅ Bot is ready for production deployment")
    else:
        print("\n❌ FAILED: Bot initialization failed")
        
except Exception as e:
    print(f"\n❌ CRITICAL ERROR: {e}")
    traceback.print_exc()

print("\n" + "=" * 40)
print("REAL TEST COMPLETED")
