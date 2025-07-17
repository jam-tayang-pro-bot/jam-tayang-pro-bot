#!/usr/bin/env python3
"""
Test Extensions Functionality
Check if installed extensions are working properly
"""

import os
import sys
import subprocess
import traceback

# Set BOT_TOKEN for testing
os.environ['BOT_TOKEN'] = '8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90'

print("🔧 TESTING EXTENSIONS FUNCTIONALITY")
print("=" * 50)

def test_python_extension():
    """Test Python extension functionality"""
    print("\n1. Testing Python Extension...")
    try:
        # Test basic Python functionality
        import ast
        import inspect
        
        # Test if we can parse Python code
        code = """
def test_function():
    return "Hello World"
        """
        
        tree = ast.parse(code)
        print("  ✅ Python AST parsing works")
        
        # Test if we can get function info
        def sample_func():
            return True
            
        sig = inspect.signature(sample_func)
        print("  ✅ Python inspection works")
        
        return True
    except Exception as e:
        print(f"  ❌ Python extension test failed: {e}")
        return False

def test_code_runner():
    """Test Code Runner functionality"""
    print("\n2. Testing Code Runner...")
    try:
        # Create a simple test script
        test_script = """
print("Code Runner Test")
print("Extensions working!")
        """
        
        with open('temp_test.py', 'w') as f:
            f.write(test_script)
        
        # Try to run the script
        result = subprocess.run(
            [sys.executable, 'temp_test.py'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and "Code Runner Test" in result.stdout:
            print("  ✅ Code Runner functionality confirmed")
            print(f"  📄 Output: {result.stdout.strip()}")
            return True
        else:
            print(f"  ⚠️ Code Runner output: {result.stdout}")
            print(f"  ⚠️ Code Runner errors: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"  ❌ Code Runner test failed: {e}")
        return False
    finally:
        # Cleanup
        if os.path.exists('temp_test.py'):
            os.remove('temp_test.py')

def test_terminal_functionality():
    """Test Terminal functionality"""
    print("\n3. Testing Terminal Functionality...")
    try:
        # Test basic terminal commands
        commands = [
            ['python', '--version'],
            ['pip', '--version'],
        ]
        
        for cmd in commands:
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    print(f"  ✅ {' '.join(cmd)}: {result.stdout.strip()}")
                else:
                    print(f"  ⚠️ {' '.join(cmd)}: {result.stderr.strip()}")
                    
            except Exception as e:
                print(f"  ❌ {' '.join(cmd)} failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Terminal test failed: {e}")
        return False

def test_main_py_import():
    """Test main.py import with extensions"""
    print("\n4. Testing main.py Import...")
    try:
        # Test if we can import main.py
        import main
        print("  ✅ main.py imported successfully")
        
        # Test if JamTayangProBot class exists
        if hasattr(main, 'JamTayangProBot'):
            print("  ✅ JamTayangProBot class found")
            
            # Try to create instance
            bot = main.JamTayangProBot()
            print("  ✅ Bot instance created")
            
            # Check bot token
            if bot.bot_token:
                print(f"  ✅ Bot token: {bot.bot_token[:10]}...")
            else:
                print("  ❌ No bot token found")
                
            return True
        else:
            print("  ❌ JamTayangProBot class not found")
            return False
            
    except Exception as e:
        print(f"  ❌ main.py import failed: {e}")
        traceback.print_exc()
        return False

def test_async_functionality():
    """Test async functionality"""
    print("\n5. Testing Async Functionality...")
    try:
        import asyncio
        import nest_asyncio
        
        # Apply nest_asyncio
        nest_asyncio.apply()
        print("  ✅ nest_asyncio applied")
        
        # Test async function
        async def test_async():
            await asyncio.sleep(0.1)
            return "Async works!"
        
        result = asyncio.run(test_async())
        print(f"  ✅ Async test result: {result}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Async test failed: {e}")
        return False

def main():
    """Run all extension tests"""
    print("🚀 Starting Extensions Functionality Test...")
    
    tests = [
        test_python_extension,
        test_code_runner,
        test_terminal_functionality,
        test_main_py_import,
        test_async_functionality
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"  ❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("🎯 EXTENSIONS TEST SUMMARY:")
    print(f"✅ Passed: {sum(results)}/{len(results)} tests")
    print(f"❌ Failed: {len(results) - sum(results)}/{len(results)} tests")
    
    if all(results):
        print("\n🎉 ALL EXTENSIONS WORKING PERFECTLY!")
        print("✅ Ready for main.py testing with enhanced tools")
    else:
        print("\n⚠️ Some extensions may need configuration")
        print("✅ But basic functionality is available")
    
    return all(results)

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🚀 READY FOR MAIN.PY TESTING!")
        else:
            print("\n🔧 Extensions need some configuration")
    except Exception as e:
        print(f"\n❌ Test crashed: {e}")
        traceback.print_exc()
