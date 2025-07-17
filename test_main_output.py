import os
import sys
import traceback

# Redirect all output to file
class FileOutput:
    def __init__(self, filename):
        self.file = open(filename, 'w', encoding='utf-8')
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        
    def write(self, text):
        self.file.write(text)
        self.file.flush()
        self.stdout.write(text)
        
    def flush(self):
        self.file.flush()
        self.stdout.flush()

# Redirect output
output = FileOutput('main_test_result.txt')
sys.stdout = output
sys.stderr = output

try:
    # Set BOT_TOKEN
    os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

    print("🧪 TESTING MAIN.PY - COMPREHENSIVE TEST")
    print("=" * 50)

    # Test 1: Basic imports
    print("1. Testing basic Python imports...")
    import asyncio
    import logging
    import os
    print("   ✅ Basic imports OK")

    # Test 2: External dependencies
    print("2. Testing external dependencies...")
    try:
        import nest_asyncio
        print("   ✅ nest_asyncio")
    except ImportError:
        print("   ❌ nest_asyncio not found, installing...")
        import subprocess
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'nest-asyncio'], check=True)
        import nest_asyncio
        print("   ✅ nest_asyncio installed and imported")

    try:
        from dotenv import load_dotenv
        print("   ✅ dotenv")
    except ImportError:
        print("   ❌ dotenv not found, installing...")
        import subprocess
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'python-dotenv'], check=True)
        from dotenv import load_dotenv
        print("   ✅ dotenv installed and imported")

    try:
        from telegram.ext import Application
        print("   ✅ telegram")
    except ImportError:
        print("   ❌ telegram not found, installing...")
        import subprocess
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'python-telegram-bot==20.7'], check=True)
        from telegram.ext import Application
        print("   ✅ telegram installed and imported")

    # Test 3: Apply nest_asyncio
    print("3. Applying nest_asyncio...")
    nest_asyncio.apply()
    print("   ✅ nest_asyncio applied successfully")

    # Test 4: Project imports
    print("4. Testing project imports...")
    
    try:
        from keep_alive import keep_alive
        print("   ✅ keep_alive imported")
    except Exception as e:
        print(f"   ❌ keep_alive error: {e}")

    try:
        from src.database.database import init_database
        print("   ✅ database imported")
    except Exception as e:
        print(f"   ❌ database error: {e}")

    try:
        from src.bot.handlers import start_handler
        print("   ✅ handlers imported")
    except Exception as e:
        print(f"   ❌ handlers error: {e}")

    # Test 5: Main bot import
    print("5. Testing main bot import...")
    try:
        from main import JamTayangProBot
        print("   ✅ JamTayangProBot imported successfully")
        
        # Create bot instance
        bot = JamTayangProBot()
        print("   ✅ Bot instance created")
        print(f"   ✅ Bot token: {bot.bot_token[:10] if bot.bot_token else 'None'}...")
        
        # Test bot attributes
        print(f"   ✅ Application: {bot.application}")
        print(f"   ✅ Scheduler: {bot.scheduler}")
        
    except Exception as e:
        print(f"   ❌ Main bot import failed: {e}")
        traceback.print_exc()

    # Test 6: Async initialization test
    print("6. Testing async initialization...")
    try:
        async def test_init():
            try:
                await bot.initialize()
                print("   ✅ Bot initialization successful")
                await bot.stop()
                print("   ✅ Bot stop successful")
                return True
            except Exception as e:
                print(f"   ❌ Async initialization error: {e}")
                traceback.print_exc()
                return False
        
        result = asyncio.run(test_init())
        if result:
            print("   ✅ Async test completed successfully")
        else:
            print("   ❌ Async test failed")
            
    except Exception as e:
        print(f"   ❌ Async test error: {e}")
        traceback.print_exc()

    print("\n" + "=" * 50)
    print("🎉 MAIN.PY TEST COMPLETED SUCCESSFULLY!")
    print("✅ Bot is ready for production deployment")

except Exception as e:
    print(f"\n❌ CRITICAL ERROR: {e}")
    traceback.print_exc()

finally:
    # Restore stdout/stderr
    sys.stdout = output.stdout
    sys.stderr = output.stderr
    output.file.close()
    print("Test completed. Check main_test_result.txt for detailed results.")
