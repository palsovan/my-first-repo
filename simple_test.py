#!/usr/bin/env python3
"""Simple test of timezone converter functionality."""

import sys
import traceback

def test_basic_functionality():
    """Test basic timezone converter functionality."""
    try:
        print("Testing timezone converter import...")
        from timezone_converter import TimezoneConverter
        print("✓ Import successful")
        
        print("Testing initialization...")
        converter = TimezoneConverter()
        print(f"✓ Initialization successful, found {len(converter.available_zones)} timezones")
        
        print("Testing UTC validation...")
        is_valid = converter.validate_timezone('UTC')
        print(f"✓ UTC validation: {is_valid}")
        
        if is_valid:
            print("Testing current UTC time...")
            current_time = converter.get_current_time('UTC')
            print(f"✓ Current UTC time: {current_time}")
            
            print("Testing basic time conversion...")
            converted = converter.convert_time('2023-06-15 12:00:00', 'UTC', 'UTC')
            print(f"✓ Conversion test: {converted}")
        
        print("Testing common timezones list...")
        common = converter.list_common_timezones()
        print(f"✓ Found {len(common)} common timezones")
        
        print("Testing timezone search...")
        results = converter.search_timezones('UTC')
        print(f"✓ Search for 'UTC' found {len(results)} results")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("Traceback:")
        traceback.print_exc()
        return False

def test_calculator():
    """Test that existing calculator still works."""
    try:
        print("\nTesting calculator import...")
        from calculator import Calculator
        print("✓ Calculator import successful")
        
        calc = Calculator()
        result = calc.add(2, 3)
        print(f"✓ Calculator test: 2 + 3 = {result}")
        
        return True
    except Exception as e:
        print(f"✗ Calculator error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("SIMPLE FUNCTIONALITY TEST")
    print("=" * 50)
    
    success1 = test_basic_functionality()
    success2 = test_calculator()
    
    print("\n" + "=" * 50)
    print("RESULTS:")
    print(f"Timezone Converter: {'PASS' if success1 else 'FAIL'}")
    print(f"Calculator: {'PASS' if success2 else 'FAIL'}")
    print("=" * 50)
    
    if success1 and success2:
        print("🎉 All basic tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)