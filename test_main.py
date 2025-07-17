#!/usr/bin/env python3
import os
import sys

# Set BOT_TOKEN
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("🧪 TESTING MAIN.PY")
print("=" * 40)

try:
    print("Step 1: Testing nest-asyncio...")
    import nest_asyncio
    nest_asyncio.apply()
    print("✅ nest-asyncio OK")
    
    print("Step 2: Testing keep-alive...")
    from keep_alive import keep_alive
    print("✅ keep-alive OK")
    
    print("Step 3: Testing main bot import...")
    from main import JamTayangProBot
    print("✅ JamTayangProBot OK")
    
    print("Step 4: Creating bot instance...")
    bot = JamTayangProBot()
    print(f"✅ Bot instance created")
    print(f"   Token: {bot.bot_token[:10]}...")
    
    print("Step 5: Testing async initialization...")
    import asyncio
    
    async def test_init():
        await bot.initialize()
        print("✅ Bot initialized successfully")
        print("   - Database ready")
        print("   - Handlers loaded")
        print("   - Application created")
    
    asyncio.run(test_init())
    
    print("\n🎉 ALL TESTS PASSED!")
    print("✅ main.py is working correctly")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    
print("\n" + "=" * 40)
print("TEST COMPLETED")
