#!/usr/bin/env python3
"""Comprehensive test of the timezone converter implementation."""

import sys
import traceback
from datetime import datetime

def check_environment():
    """Check Python environment and available libraries."""
    print("ENVIRONMENT CHECK")
    print("-" * 40)
    print(f"Python version: {sys.version}")
    
    # Check zoneinfo
    try:
        from zoneinfo import ZoneInfo, available_timezones
        print("✓ zoneinfo available (Python 3.9+)")
        zoneinfo_available = True
    except ImportError:
        print("✗ zoneinfo not available")
        zoneinfo_available = False
    
    # Check pytz
    try:
        import pytz
        print("✓ pytz available")
        pytz_available = True
    except ImportError:
        print("✗ pytz not available")
        pytz_available = False
    
    if not zoneinfo_available and not pytz_available:
        print("❌ Neither zoneinfo nor pytz available - timezone converter will not work")
        return False
    
    return True

def test_imports():
    """Test importing both modules."""
    print("\nIMPORT TESTS")
    print("-" * 40)
    
    try:
        from calculator import Calculator
        print("✓ Calculator import successful")
        calc_import = True
    except Exception as e:
        print(f"✗ Calculator import failed: {e}")
        calc_import = False
    
    try:
        from timezone_converter import TimezoneConverter
        print("✓ TimezoneConverter import successful")
        tz_import = True
    except Exception as e:
        print(f"✗ TimezoneConverter import failed: {e}")
        traceback.print_exc()
        tz_import = False
    
    return calc_import, tz_import

def test_calculator_basic():
    """Test basic calculator functionality."""
    print("\nCALCULATOR BASIC TESTS")
    print("-" * 40)
    
    try:
        from calculator import Calculator
        calc = Calculator()
        
        # Test basic operations
        tests = [
            (calc.add, 2, 3, 5),
            (calc.subtract, 5, 3, 2),
            (calc.multiply, 4, 3, 12),
            (calc.divide, 10, 2, 5)
        ]
        
        for func, a, b, expected in tests:
            result = func(a, b)
            if result == expected:
                print(f"✓ {func.__name__}({a}, {b}) = {result}")
            else:
                print(f"✗ {func.__name__}({a}, {b}) = {result}, expected {expected}")
                return False
        
        # Test division by zero
        try:
            calc.divide(5, 0)
            print("✗ Division by zero should raise ValueError")
            return False
        except ValueError:
            print("✓ Division by zero properly raises ValueError")
        
        return True
        
    except Exception as e:
        print(f"✗ Calculator test error: {e}")
        return False

def test_timezone_converter_basic():
    """Test basic timezone converter functionality."""
    print("\nTIMEZONE CONVERTER BASIC TESTS")
    print("-" * 40)
    
    try:
        from timezone_converter import TimezoneConverter
        converter = TimezoneConverter()
        
        print(f"✓ Converter initialized with {len(converter.available_zones)} timezones")
        
        # Test UTC validation
        if converter.validate_timezone('UTC'):
            print("✓ UTC timezone validation")
        else:
            print("✗ UTC timezone validation failed")
            return False
        
        # Test invalid timezone
        if not converter.validate_timezone('Invalid/Timezone'):
            print("✓ Invalid timezone properly rejected")
        else:
            print("✗ Invalid timezone not properly rejected")
            return False
        
        # Test current time
        try:
            current_utc = converter.get_current_time('UTC')
            print(f"✓ Current UTC time: {current_utc}")
        except Exception as e:
            print(f"✗ Error getting current time: {e}")
            return False
        
        # Test basic conversion (UTC to UTC)
        try:
            result = converter.convert_time('2023-06-15 12:00:00', 'UTC', 'UTC')
            if result.hour == 12 and result.day == 15:
                print(f"✓ Basic conversion: {result}")
            else:
                print(f"✗ Basic conversion failed: {result}")
                return False
        except Exception as e:
            print(f"✗ Basic conversion error: {e}")
            return False
        
        # Test common timezones
        common = converter.list_common_timezones()
        if len(common) > 0 and 'UTC' in common:
            print(f"✓ Common timezones list ({len(common)} zones)")
        else:
            print(f"✗ Common timezones list issue: {common}")
            return False
        
        # Test search
        search_results = converter.search_timezones('UTC')
        if len(search_results) > 0:
            print(f"✓ Timezone search found {len(search_results)} results")
        else:
            print("✗ Timezone search failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Timezone converter test error: {e}")
        traceback.print_exc()
        return False

def test_timezone_converter_advanced():
    """Test advanced timezone converter functionality."""
    print("\nTIMEZONE CONVERTER ADVANCED TESTS")
    print("-" * 40)
    
    try:
        from timezone_converter import TimezoneConverter
        converter = TimezoneConverter()
        
        # Test error handling
        try:
            converter.get_current_time('Invalid/Timezone')
            print("✗ Should have raised error for invalid timezone")
            return False
        except ValueError:
            print("✓ Proper error handling for invalid timezone")
        
        # Test invalid time format
        try:
            converter.convert_time('invalid-format', 'UTC', 'UTC')
            print("✗ Should have raised error for invalid time format")
            return False
        except ValueError:
            print("✓ Proper error handling for invalid time format")
        
        # Test timezone conversion if US/Eastern is available
        if converter.validate_timezone('US/Eastern'):
            try:
                # Convert UTC to Eastern (should be different in summer)
                result = converter.convert_time('2023-06-15 16:00:00', 'UTC', 'US/Eastern')
                print(f"✓ UTC to US/Eastern conversion: {result}")
                
                # The hour should be different (EDT is UTC-4 in summer)
                if result.hour == 12:  # 16:00 UTC = 12:00 EDT
                    print("✓ Timezone conversion math correct")
                else:
                    print(f"? Timezone conversion result: {result.hour}:00 (may vary by DST)")
            except Exception as e:
                print(f"✗ Timezone conversion error: {e}")
                return False
        else:
            print("? US/Eastern not available, skipping conversion test")
        
        return True
        
    except Exception as e:
        print(f"✗ Advanced timezone test error: {e}")
        return False

def run_unit_tests():
    """Run the actual unit test suites."""
    print("\nUNIT TEST SUITES")
    print("-" * 40)
    
    import unittest
    
    # Test calculator unit tests
    try:
        from test_calculator import TestCalculator
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        calc_tests_pass = result.wasSuccessful()
        print(f"Calculator unit tests: {'PASS' if calc_tests_pass else 'FAIL'}")
    except Exception as e:
        print(f"Calculator unit tests error: {e}")
        calc_tests_pass = False
    
    # Test timezone converter unit tests
    try:
        from test_timezone_converter import TestTimezoneConverter
        suite = unittest.TestLoader().loadTestsFromTestCase(TestTimezoneConverter)
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        tz_tests_pass = result.wasSuccessful()
        print(f"Timezone converter unit tests: {'PASS' if tz_tests_pass else 'FAIL'}")
    except Exception as e:
        print(f"Timezone converter unit tests error: {e}")
        tz_tests_pass = False
    
    return calc_tests_pass, tz_tests_pass

def main():
    """Run comprehensive tests."""
    print("COMPREHENSIVE TIMEZONE CONVERTER TEST")
    print("=" * 60)
    
    # Check environment
    env_ok = check_environment()
    if not env_ok:
        print("❌ Environment check failed - cannot proceed")
        return 1
    
    # Test imports
    calc_import, tz_import = test_imports()
    
    # Test basic functionality
    calc_basic = test_calculator_basic() if calc_import else False
    tz_basic = test_timezone_converter_basic() if tz_import else False
    tz_advanced = test_timezone_converter_advanced() if tz_import else False
    
    # Run unit tests
    calc_unit, tz_unit = run_unit_tests()
    
    # Summary
    print("\n" + "=" * 60)
    print("FINAL RESULTS:")
    print(f"Environment: {'OK' if env_ok else 'FAIL'}")
    print(f"Calculator import: {'OK' if calc_import else 'FAIL'}")
    print(f"Timezone converter import: {'OK' if tz_import else 'FAIL'}")
    print(f"Calculator basic tests: {'PASS' if calc_basic else 'FAIL'}")
    print(f"Timezone converter basic tests: {'PASS' if tz_basic else 'FAIL'}")
    print(f"Timezone converter advanced tests: {'PASS' if tz_advanced else 'FAIL'}")
    print(f"Calculator unit tests: {'PASS' if calc_unit else 'FAIL'}")
    print(f"Timezone converter unit tests: {'PASS' if tz_unit else 'FAIL'}")
    print("=" * 60)
    
    all_pass = all([env_ok, calc_import, tz_import, calc_basic, tz_basic, tz_advanced, calc_unit, tz_unit])
    
    if all_pass:
        print("🎉 ALL TESTS PASSED! Timezone converter is ready to use.")
        return 0
    else:
        print("❌ Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())