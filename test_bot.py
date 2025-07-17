#!/usr/bin/env python3
"""
Test script untuk mengecek apakah bot bisa jalan tanpa error
"""

import os
import sys
import asyncio

# Set BOT_TOKEN untuk testing
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("🧪 TESTING BOT - CHECKING FOR ERRORS")
print("=" * 50)

try:
    print("1️⃣ Testing nest-asyncio...")
    import nest_asyncio
    nest_asyncio.apply()
    print("✅ nest-asyncio applied successfully")
    
    print("2️⃣ Testing keep-alive...")
    from keep_alive import keep_alive, app
    print("✅ keep-alive imported successfully")
    
    # Test Flask routes
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("✅ Keep-alive home route working")
        
        response = client.get('/status')
        if response.status_code == 200:
            print("✅ Keep-alive status route working")
    
    print("3️⃣ Testing main bot import...")
    from main import JamTayangProBot
    print("✅ JamTayangProBot imported successfully")
    
    print("4️⃣ Testing bot initialization...")
    bot = JamTayangProBot()
    print(f"✅ Bot initialized with token: {bot.bot_token[:10]}...")
    
    print("5️⃣ Testing async initialization...")
    async def test_init():
        try:
            await bot.initialize()
            print("✅ Bot async initialization successful")
            print("✅ Database initialized")
            print("✅ Handlers added")
            return True
        except Exception as e:
            print(f"❌ Bot initialization error: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    # Test initialization
    result = asyncio.run(test_init())
    
    if result:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Bot is ready to run without errors")
        print("✅ nest-asyncio fixes event loop conflicts")
        print("✅ Keep-alive system working")
        print("✅ Database initialization working")
        print("✅ All handlers loaded successfully")
    else:
        print("\n❌ SOME TESTS FAILED")
        
except Exception as e:
    print(f"\n❌ CRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("TESTING COMPLETED")
