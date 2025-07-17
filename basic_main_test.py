import os
import sys

# Set BOT_TOKEN
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("TESTING MAIN.PY")
print("=" * 30)

# Test 1: Basic imports
print("1. Basic imports...")
try:
    import asyncio
    import logging
    import os
    print("   OK: Built-in modules")
except Exception as e:
    print(f"   ERROR: Built-in modules failed: {e}")
    sys.exit(1)

# Test 2: External dependencies
print("2. External dependencies...")
try:
    import nest_asyncio
    print("   OK: nest_asyncio")
except Exception as e:
    print(f"   ERROR: nest_asyncio: {e}")

try:
    from dotenv import load_dotenv
    print("   OK: dotenv")
except Exception as e:
    print(f"   ERROR: dotenv: {e}")

try:
    from telegram.ext import Application
    print("   OK: telegram")
except Exception as e:
    print(f"   ERROR: telegram: {e}")

# Test 3: Project files
print("3. Project imports...")
try:
    from keep_alive import keep_alive
    print("   OK: keep_alive")
except Exception as e:
    print(f"   ERROR: keep_alive: {e}")

try:
    from src.database.database import init_database
    print("   OK: database")
except Exception as e:
    print(f"   ERROR: database: {e}")

try:
    from src.bot.handlers import start_handler
    print("   OK: handlers")
except Exception as e:
    print(f"   ERROR: handlers: {e}")

# Test 4: Main bot
print("4. Main bot import...")
try:
    from main import JamTayangProBot
    print("   OK: JamTayangProBot imported")
    
    bot = JamTayangProBot()
    print("   OK: Bot instance created")
    if bot.bot_token:
        print(f"   OK: Token: {bot.bot_token[:10]}...")
    else:
        print("   WARNING: No token found")
    
except Exception as e:
    print(f"   ERROR: Main bot failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 30)
print("TEST COMPLETED")
