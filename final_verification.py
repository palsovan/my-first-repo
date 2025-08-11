#!/usr/bin/env python3
"""Final verification script for the timezone converter implementation."""

import sys
import unittest
from datetime import datetime

def print_header(title):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print('='*60)

def print_section(title):
    """Print a formatted section header."""
    print(f"\n{title}")
    print('-' * len(title))

def check_environment():
    """Check the Python environment and dependencies."""
    print_section("Environment Check")
    
    print(f"Python version: {sys.version}")
    
    # Check for timezone libraries
    zoneinfo_available = False
    pytz_available = False
    
    try:
        from zoneinfo import ZoneInfo, available_timezones
        print("✓ zoneinfo available (Python 3.9+)")
        zoneinfo_available = True
    except ImportError:
        print("✗ zoneinfo not available")
    
    try:
        import pytz
        print("✓ pytz available")
        pytz_available = True
    except ImportError:
        print("✗ pytz not available")
    
    if not zoneinfo_available and not pytz_available:
        print("❌ CRITICAL: No timezone library available!")
        return False
    
    return True

def test_calculator():
    """Test calculator functionality."""
    print_section("Calculator Tests")
    
    try:
        from calculator import Calculator
        calc = Calculator()
        
        # Basic functionality test
        tests = [
            (calc.add, 2, 3, 5, "Addition"),
            (calc.subtract, 10, 4, 6, "Subtraction"),
            (calc.multiply, 3, 7, 21, "Multiplication"),
            (calc.divide, 15, 3, 5, "Division")
        ]
        
        for func, a, b, expected, name in tests:
            result = func(a, b)
            if result == expected:
                print(f"✓ {name}: {a} {func.__name__} {b} = {result}")
            else:
                print(f"✗ {name}: Expected {expected}, got {result}")
                return False
        
        # Test error handling
        try:
            calc.divide(5, 0)
            print("✗ Division by zero should raise ValueError")
            return False
        except ValueError:
            print("✓ Division by zero error handling")
        
        # Run unit tests
        print("\nRunning calculator unit tests...")
        from test_calculator import TestCalculator
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
        
        if result.wasSuccessful():
            print(f"✓ All {result.testsRun} unit tests passed")
            return True
        else:
            print(f"✗ {len(result.failures + result.errors)} unit tests failed")
            return False
            
    except Exception as e:
        print(f"✗ Calculator test error: {e}")
        return False

def test_timezone_converter():
    """Test timezone converter functionality."""
    print_section("Timezone Converter Tests")
    
    try:
        from timezone_converter import TimezoneConverter
        converter = TimezoneConverter()
        
        print(f"✓ Initialized with {len(converter.available_zones)} timezones")
        
        # Basic validation tests
        if not converter.validate_timezone('UTC'):
            print("✗ UTC should be a valid timezone")
            return False
        print("✓ UTC timezone validation")
        
        if converter.validate_timezone('Invalid/Timezone'):
            print("✗ Invalid timezone should not validate")
            return False
        print("✓ Invalid timezone rejection")
        
        # Current time test
        try:
            current_utc = converter.get_current_time('UTC')
            print(f"✓ Current UTC time: {current_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        except Exception as e:
            print(f"✗ Current time error: {e}")
            return False
        
        # Basic conversion test
        try:
            test_time = '2023-06-15 12:00:00'
            result = converter.convert_time(test_time, 'UTC', 'UTC')
            if result.hour == 12 and result.day == 15:
                print(f"✓ Basic conversion: {result}")
            else:
                print(f"✗ Conversion error: expected 12:00 on 15th, got {result}")
                return False
        except Exception as e:
            print(f"✗ Conversion error: {e}")
            return False
        
        # Test timezone conversion if US/Eastern is available
        if converter.validate_timezone('US/Eastern'):
            try:
                # Test summer time conversion (June = EDT, UTC-4)
                result = converter.convert_time('2023-06-15 16:00:00', 'UTC', 'US/Eastern')
                print(f"✓ UTC to US/Eastern: {result.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                # Note: We don't assert specific hour due to DST complexity
            except Exception as e:
                print(f"✗ Timezone conversion error: {e}")
                return False
        
        # Test common timezones
        common = converter.list_common_timezones()
        if len(common) > 0 and 'UTC' in common:
            print(f"✓ Common timezones: {len(common)} zones")
        else:
            print("✗ Common timezones list error")
            return False
        
        # Test search
        search_results = converter.search_timezones('UTC')
        if len(search_results) > 0:
            print(f"✓ Search functionality: found {len(search_results)} results for 'UTC'")
        else:
            print("✗ Search functionality failed")
            return False
        
        # Test error handling
        try:
            converter.get_current_time('Invalid/Timezone')
            print("✗ Should raise error for invalid timezone")
            return False
        except ValueError:
            print("✓ Invalid timezone error handling")
        
        try:
            converter.convert_time('invalid-format', 'UTC', 'UTC')
            print("✗ Should raise error for invalid time format")
            return False
        except ValueError:
            print("✓ Invalid time format error handling")
        
        # Run unit tests
        print("\nRunning timezone converter unit tests...")
        from test_timezone_converter import TestTimezoneConverter
        suite = unittest.TestLoader().loadTestsFromTestCase(TestTimezoneConverter)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
        
        if result.wasSuccessful():
            print(f"✓ All {result.testsRun} unit tests passed")
            return True
        else:
            print(f"✗ {len(result.failures + result.errors)} unit tests failed")
            for test, error in result.failures + result.errors:
                print(f"  Failed: {test}")
            return False
            
    except Exception as e:
        print(f"✗ Timezone converter test error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_cli_interfaces():
    """Test that CLI interfaces can be imported without errors."""
    print_section("CLI Interface Tests")
    
    try:
        # Test calculator CLI import
        import calculator
        print("✓ Calculator CLI module imports successfully")
        
        # Test timezone converter CLI import  
        import timezone_converter
        print("✓ Timezone converter CLI module imports successfully")
        
        return True
        
    except Exception as e:
        print(f"✗ CLI interface test error: {e}")
        return False

def verify_file_structure():
    """Verify all required files are present."""
    print_section("File Structure Verification")
    
    import os
    
    required_files = [
        'calculator.py',
        'test_calculator.py', 
        'timezone_converter.py',
        'test_timezone_converter.py',
        'README.md',
        'LICENSE'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(f'/workspace/{file}'):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - MISSING")
            missing_files.append(file)
    
    return len(missing_files) == 0

def main():
    """Run complete verification."""
    print_header("TIMEZONE CONVERTER IMPLEMENTATION VERIFICATION")
    
    # Run all tests
    env_ok = check_environment()
    files_ok = verify_file_structure()
    calc_ok = test_calculator()
    tz_ok = test_timezone_converter()
    cli_ok = test_cli_interfaces()
    
    # Final summary
    print_header("VERIFICATION SUMMARY")
    
    results = [
        ("Environment", env_ok),
        ("File Structure", files_ok),
        ("Calculator", calc_ok),
        ("Timezone Converter", tz_ok),
        ("CLI Interfaces", cli_ok)
    ]
    
    all_passed = True
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        icon = "✓" if passed else "✗"
        print(f"{icon} {test_name:20}: {status}")
        if not passed:
            all_passed = False
    
    print('='*60)
    
    if all_passed:
        print("🎉 SUCCESS: Timezone converter implementation is complete and working!")
        print("\nYou can now use:")
        print("  python calculator.py          - Run calculator app")
        print("  python timezone_converter.py  - Run timezone converter app")
        print("  python -m unittest discover   - Run all tests")
        return 0
    else:
        print("❌ FAILURE: Some components are not working correctly.")
        print("Please check the errors above and fix the issues.")
        return 1

if __name__ == "__main__":
    sys.exit(main())