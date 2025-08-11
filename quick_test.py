#!/usr/bin/env python3
"""Quick test to verify timezone converter works."""

def main():
    print("Quick Timezone Converter Test")
    print("=" * 40)
    
    # Test 1: Check if we can import
    try:
        from timezone_converter import TimezoneConverter
        print("✓ Import successful")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False
    
    # Test 2: Initialize
    try:
        converter = TimezoneConverter()
        print(f"✓ Initialized with {len(converter.available_zones)} timezones")
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return False
    
    # Test 3: Basic validation
    try:
        utc_valid = converter.validate_timezone('UTC')
        invalid_valid = converter.validate_timezone('Invalid/Zone')
        print(f"✓ Validation: UTC={utc_valid}, Invalid={invalid_valid}")
        if not utc_valid or invalid_valid:
            print("✗ Validation logic error")
            return False
    except Exception as e:
        print(f"✗ Validation failed: {e}")
        return False
    
    # Test 4: Current time
    try:
        current = converter.get_current_time('UTC')
        print(f"✓ Current UTC time: {current}")
    except Exception as e:
        print(f"✗ Current time failed: {e}")
        return False
    
    # Test 5: Basic conversion
    try:
        result = converter.convert_time('2023-06-15 12:00:00', 'UTC', 'UTC')
        print(f"✓ Basic conversion: {result}")
        if result.hour != 12:
            print("✗ Conversion logic error")
            return False
    except Exception as e:
        print(f"✗ Conversion failed: {e}")
        return False
    
    print("✓ All basic tests passed!")
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("🎉 Timezone converter is working!")
    else:
        print("❌ Issues detected")
    exit(0 if success else 1)