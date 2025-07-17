import os
import sys
import traceback

# Redirect output to file
with open('test_output.txt', 'w') as f:
    f.write("🧪 TESTING MAIN.PY\n")
    f.write("=" * 40 + "\n")
    
    try:
        # Set BOT_TOKEN
        os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'
        f.write("✅ BOT_TOKEN set\n")
        
        # Test imports one by one
        f.write("Testing imports...\n")
        
        import nest_asyncio
        f.write("✅ nest_asyncio imported\n")
        
        nest_asyncio.apply()
        f.write("✅ nest_asyncio applied\n")
        
        from dotenv import load_dotenv
        f.write("✅ dotenv imported\n")
        
        from telegram.ext import Application
        f.write("✅ telegram imported\n")
        
        from src.database.database import init_database
        f.write("✅ database imported\n")
        
        from src.bot.handlers import start_handler
        f.write("✅ handlers imported\n")
        
        from main import JamTayangProBot
        f.write("✅ JamTayangProBot imported\n")
        
        # Test bot creation
        bot = JamTayangProBot()
        f.write(f"✅ Bot created with token: {bot.bot_token[:10]}...\n")
        
        f.write("\n🎉 ALL IMPORTS SUCCESSFUL!\n")
        
    except Exception as e:
        f.write(f"\n❌ ERROR: {str(e)}\n")
        f.write(traceback.format_exc())
    
    f.write("\n" + "=" * 40 + "\n")
    f.write("TEST COMPLETED\n")

print("Test completed. Check test_output.txt for results.")
