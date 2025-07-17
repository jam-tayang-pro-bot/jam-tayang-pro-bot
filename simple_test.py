print("🧪 SIMPLE BOT TEST")
print("=" * 30)

# Test imports
try:
    import nest_asyncio
    print("✅ nest-asyncio OK")
except:
    print("❌ nest-asyncio FAILED")

try:
    from keep_alive import keep_alive
    print("✅ keep-alive OK")
except Exception as e:
    print(f"❌ keep-alive FAILED: {e}")

try:
    from main import JamTayangProBot
    print("✅ main bot OK")
except Exception as e:
    print(f"❌ main bot FAILED: {e}")

print("=" * 30)
print("TEST COMPLETED")
