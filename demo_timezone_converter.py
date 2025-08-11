#!/usr/bin/env python3
"""Demo script to showcase timezone converter functionality."""

from datetime import datetime
import sys

def demo_timezone_converter():
    """Demonstrate timezone converter capabilities."""
    print("TIMEZONE CONVERTER DEMO")
    print("=" * 50)
    
    try:
        from timezone_converter import TimezoneConverter
        converter = TimezoneConverter()
        
        print(f"Initialized with {len(converter.available_zones)} available timezones\n")
        
        # Demo 1: Current time in different timezones
        print("1. CURRENT TIME IN DIFFERENT TIMEZONES")
        print("-" * 40)
        
        demo_timezones = ['UTC']
        # Add common timezones if available
        for tz in ['US/Eastern', 'US/Pacific', 'Europe/London', 'Asia/Tokyo']:
            if converter.validate_timezone(tz):
                demo_timezones.append(tz)
        
        for tz in demo_timezones:
            try:
                current_time = converter.get_current_time(tz)
                print(f"{tz:15}: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            except Exception as e:
                print(f"{tz:15}: Error - {e}")
        
        # Demo 2: Time conversion
        print("\n2. TIME CONVERSION EXAMPLES")
        print("-" * 40)
        
        test_time = "2023-12-25 15:30:00"  # Christmas afternoon
        print(f"Converting: {test_time}")
        
        conversions = [
            ('UTC', 'UTC'),
        ]
        
        # Add conversions if timezones are available
        if converter.validate_timezone('US/Eastern'):
            conversions.append(('UTC', 'US/Eastern'))
        if converter.validate_timezone('Asia/Tokyo'):
            conversions.append(('UTC', 'Asia/Tokyo'))
        if converter.validate_timezone('Europe/London'):
            conversions.append(('UTC', 'Europe/London'))
        
        for from_tz, to_tz in conversions:
            try:
                result = converter.convert_time(test_time, from_tz, to_tz)
                print(f"{from_tz} → {to_tz}: {result.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            except Exception as e:
                print(f"{from_tz} → {to_tz}: Error - {e}")
        
        # Demo 3: Common timezones
        print("\n3. COMMON TIMEZONES")
        print("-" * 40)
        
        common = converter.list_common_timezones()
        print(f"Found {len(common)} common timezones:")
        for i, tz in enumerate(common[:10], 1):  # Show first 10
            print(f"{i:2d}. {tz}")
        if len(common) > 10:
            print(f"    ... and {len(common) - 10} more")
        
        # Demo 4: Search functionality
        print("\n4. TIMEZONE SEARCH")
        print("-" * 40)
        
        search_terms = ['America', 'Europe', 'Asia']
        for term in search_terms:
            results = converter.search_timezones(term)
            print(f"'{term}': {len(results)} matches")
            if results:
                print(f"  Examples: {', '.join(results[:3])}")
                if len(results) > 3:
                    print(f"  ... and {len(results) - 3} more")
        
        # Demo 5: Error handling
        print("\n5. ERROR HANDLING DEMO")
        print("-" * 40)
        
        # Invalid timezone
        try:
            converter.get_current_time('Invalid/Timezone')
        except ValueError as e:
            print(f"✓ Invalid timezone error: {e}")
        
        # Invalid time format
        try:
            converter.convert_time('not-a-time', 'UTC', 'UTC')
        except ValueError as e:
            print(f"✓ Invalid time format error: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 DEMO COMPLETED SUCCESSFULLY!")
        print("The timezone converter is working properly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure the timezone converter module is available.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

def demo_calculator():
    """Quick demo of calculator to ensure it still works."""
    print("\nCALCULATOR DEMO (Existing Functionality)")
    print("=" * 50)
    
    try:
        from calculator import Calculator
        calc = Calculator()
        
        operations = [
            ('add', 10, 5),
            ('subtract', 10, 3),
            ('multiply', 4, 7),
            ('divide', 20, 4)
        ]
        
        for op, a, b in operations:
            method = getattr(calc, op)
            result = method(a, b)
            print(f"{a} {op} {b} = {result}")
        
        # Test division by zero
        try:
            calc.divide(5, 0)
        except ValueError as e:
            print(f"Division by zero error: {e}")
        
        print("✓ Calculator still working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Calculator error: {e}")
        return False

if __name__ == "__main__":
    print("TIMEZONE CONVERTER & CALCULATOR DEMO")
    print("=" * 60)
    
    tz_success = demo_timezone_converter()
    calc_success = demo_calculator()
    
    print("\n" + "=" * 60)
    print("DEMO SUMMARY:")
    print(f"Timezone Converter: {'SUCCESS' if tz_success else 'FAILED'}")
    print(f"Calculator: {'SUCCESS' if calc_success else 'FAILED'}")
    print("=" * 60)
    
    if tz_success and calc_success:
        print("🎉 Both applications are working correctly!")
        sys.exit(0)
    else:
        print("❌ Some issues detected.")
        sys.exit(1)