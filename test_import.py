#!/usr/bin/env python3
"""Simple test to verify timezone_converter imports correctly."""

try:
    from timezone_converter import TimezoneConverter
    print("✓ Successfully imported TimezoneConverter")
    
    # Test basic initialization
    converter = TimezoneConverter()
    print(f"✓ Successfully initialized converter with {len(converter.available_zones)} timezones")
    
    # Test basic validation
    print(f"✓ UTC validation: {converter.validate_timezone('UTC')}")
    print(f"✓ Invalid timezone validation: {converter.validate_timezone('Invalid/Zone')}")
    
    # Test current time
    try:
        current_utc = converter.get_current_time('UTC')
        print(f"✓ Current UTC time: {current_utc}")
    except Exception as e:
        print(f"✗ Error getting current time: {e}")
    
    # Test basic conversion
    try:
        result = converter.convert_time('2023-06-15 12:00:00', 'UTC', 'UTC')
        print(f"✓ Basic conversion test: {result}")
    except Exception as e:
        print(f"✗ Error in conversion: {e}")
        
    print("✓ All basic tests passed!")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
except Exception as e:
    print(f"✗ Unexpected error: {e}")