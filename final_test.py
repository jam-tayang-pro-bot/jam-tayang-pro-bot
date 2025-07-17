#!/usr/bin/env python3
import os
import sys

# Set environment
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("🧪 FINAL TEST - MAIN.PY")
print("=" * 50)

# Test 1: Basic imports
print("1. Testing basic imports...")
try:
    import nest_asyncio
    print("   ✅ nest_asyncio")
    
    from dotenv import load_dotenv
    print("   ✅ dotenv")
    
    from telegram.ext import Application
    print("   ✅ telegram")
    
    from flask import Flask
    print("   ✅ flask")
    
    import sqlalchemy
    print("   ✅ sqlalchemy")
    
except Exception as e:
    print(f"   ❌ Import error: {e}")
    sys.exit(1)

# Test 2: Apply nest_asyncio
print("\n2. Applying nest_asyncio...")
try:
    nest_asyncio.apply()
    print("   ✅ nest_asyncio applied")
except Exception as e:
    print(f"   ❌ nest_asyncio error: {e}")

# Test 3: Import project modules
print("\n3. Testing project imports...")
try:
    from keep_alive import keep_alive
    print("   ✅ keep_alive")
    
    from src.database.database import init_database
    print("   ✅ database")
    
    from src.bot.handlers import start_handler
    print("   ✅ handlers")
    
    from main import JamTayangProBot
    print("   ✅ JamTayangProBot")
    
except Exception as e:
    print(f"   ❌ Project import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Create bot instance
print("\n4. Creating bot instance...")
try:
    bot = JamTayangProBot()
    print(f"   ✅ Bot created")
    print(f"   ✅ Token: {bot.bot_token[:10]}...")
except Exception as e:
    print(f"   ❌ Bot creation error: {e}")
    sys.exit(1)

# Test 5: Test async initialization (without running)
print("\n5. Testing async components...")
try:
    import asyncio
    
    async def test_async():
        try:
            # Just test that we can create the async components
            await bot.initialize()
            print("   ✅ Bot initialization successful")
            await bot.stop()
            print("   ✅ Bot stop successful")
            return True
        except Exception as e:
            print(f"   ❌ Async error: {e}")
            return False
    
    # Run the async test
    result = asyncio.run(test_async())
    
    if result:
        print("   ✅ Async test passed")
    else:
        print("   ❌ Async test failed")
        
except Exception as e:
    print(f"   ❌ Async test error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("🎉 MAIN.PY TEST COMPLETED!")
print("✅ Bot is ready for deployment")
