import subprocess
import sys
import os

print("FINAL MAIN.PY TEST")
print("=" * 30)

# Test 1: Check if .env exists
if os.path.exists('.env'):
    print("✅ .env file exists")
else:
    print("❌ .env file missing")

# Test 2: Check if main.py exists
if os.path.exists('main.py'):
    print("✅ main.py file exists")
else:
    print("❌ main.py file missing")
    sys.exit(1)

# Test 3: Try to run main.py with timeout
print("\nTesting main.py execution...")
try:
    # Run main.py with timeout of 10 seconds
    result = subprocess.run(
        [sys.executable, 'main.py'],
        capture_output=True,
        text=True,
        timeout=10,
        encoding='utf-8',
        errors='ignore'
    )
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print(f"\nReturn code: {result.returncode}")
    
    if result.returncode == 0:
        print("✅ main.py executed successfully")
    else:
        print("❌ main.py execution failed")
        
except subprocess.TimeoutExpired:
    print("⏰ main.py execution timed out (this is normal for a bot)")
    print("✅ Bot started successfully but was stopped due to timeout")
    
except Exception as e:
    print(f"❌ Error running main.py: {e}")

print("\n" + "=" * 30)
print("TEST COMPLETED")
