import os
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("TESTING MAIN.PY")
print("================")

try:
    print("1. Testing basic imports...")
    import asyncio
    import logging
    print("   ✅ Built-in modules OK")
    
    print("2. Testing external imports...")
    try:
        import nest_asyncio
        nest_asyncio.apply()
        print("   ✅ nest_asyncio OK")
    except:
        print("   ❌ nest_asyncio failed")
    
    try:
        from dotenv import load_dotenv
        print("   ✅ dotenv OK")
    except:
        print("   ❌ dotenv failed")
    
    try:
        from telegram.ext import Application
        print("   ✅ telegram OK")
    except:
        print("   ❌ telegram failed")
    
    print("3. Testing main.py import...")
    try:
        import main
        print("   ✅ main.py imported successfully")
        
        bot = main.JamTayangProBot()
        print("   ✅ Bot instance created")
        print(f"   ✅ Bot token: {bot.bot_token[:10]}...")
        
        print("4. SUCCESS: MAIN.PY WORKS!")
        
    except Exception as e:
        print(f"   ❌ main.py failed: {e}")
        
except Exception as e:
    print(f"CRITICAL ERROR: {e}")

print("================")
print("TEST COMPLETED")
