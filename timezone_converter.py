from datetime import datetime
import sys

# Try to use zoneinfo (Python 3.9+), fallback to pytz for older versions
try:
    from zoneinfo import ZoneInfo, available_timezones
    USE_ZONEINFO = True
except ImportError:
    try:
        import pytz
        USE_ZONEINFO = False
    except ImportError:
        print("Error: This application requires either Python 3.9+ or the pytz library.")
        print("Please install pytz with: pip install pytz")
        sys.exit(1)


class TimezoneConverter:
    def __init__(self):
        if USE_ZONEINFO:
            self.available_zones = sorted(available_timezones())
        else:
            self.available_zones = sorted(pytz.all_timezones)
    
    def get_current_time(self, timezone_name):
        """Get current time in the specified timezone."""
        try:
            if USE_ZONEINFO:
                tz = ZoneInfo(timezone_name)
                return datetime.now(tz)
            else:
                tz = pytz.timezone(timezone_name)
                return datetime.now(tz)
        except Exception as e:
            raise ValueError(f"Invalid timezone '{timezone_name}': {e}")
    
    def convert_time(self, dt_str, from_tz, to_tz, time_format="%Y-%m-%d %H:%M:%S"):
        """Convert time from one timezone to another."""
        try:
            # Parse the datetime string
            dt_naive = datetime.strptime(dt_str, time_format)
            
            if USE_ZONEINFO:
                # Create timezone-aware datetime
                from_timezone = ZoneInfo(from_tz)
                to_timezone = ZoneInfo(to_tz)
                dt_aware = dt_naive.replace(tzinfo=from_timezone)
                # Convert to target timezone
                converted_dt = dt_aware.astimezone(to_timezone)
            else:
                # Using pytz
                from_timezone = pytz.timezone(from_tz)
                to_timezone = pytz.timezone(to_tz)
                # Localize the naive datetime to the source timezone
                dt_aware = from_timezone.localize(dt_naive)
                # Convert to target timezone
                converted_dt = dt_aware.astimezone(to_timezone)
            
            return converted_dt
        except ValueError as e:
            if "time data" in str(e):
                raise ValueError(f"Invalid time format. Expected format: {time_format}")
            else:
                raise ValueError(f"Invalid timezone: {e}")
        except Exception as e:
            raise ValueError(f"Conversion error: {e}")
    
    def list_common_timezones(self):
        """Return a list of commonly used timezones."""
        common_zones = [
            'UTC',
            'US/Eastern',
            'US/Central', 
            'US/Mountain',
            'US/Pacific',
            'Europe/London',
            'Europe/Paris',
            'Europe/Berlin',
            'Asia/Tokyo',
            'Asia/Shanghai',
            'Asia/Kolkata',
            'Australia/Sydney',
            'America/New_York',
            'America/Chicago',
            'America/Denver',
            'America/Los_Angeles'
        ]
        # Filter to only include zones that exist in the current system
        return [zone for zone in common_zones if zone in self.available_zones]
    
    def search_timezones(self, search_term):
        """Search for timezones containing the search term."""
        search_term = search_term.lower()
        return [zone for zone in self.available_zones if search_term in zone.lower()]
    
    def validate_timezone(self, timezone_name):
        """Check if a timezone name is valid."""
        return timezone_name in self.available_zones


def print_timezone_list(zones, title="Timezones"):
    """Helper function to print a formatted list of timezones."""
    print(f"\n{title}:")
    print("-" * len(title))
    for i, zone in enumerate(zones, 1):
        print(f"{i:2d}. {zone}")
    print()


if __name__ == "__main__":
    converter = TimezoneConverter()
    print("Welcome to the Timezone Converter App!")
    print("Available commands: current, convert, list, search, quit")
    
    while True:
        command = input("\nEnter command: ").lower().strip()
        
        if command == 'quit':
            break
        elif command == 'current':
            timezone = input("Enter timezone (or 'list' to see options): ").strip()
            if timezone.lower() == 'list':
                print_timezone_list(converter.list_common_timezones(), "Common Timezones")
                continue
            
            try:
                current_time = converter.get_current_time(timezone)
                print(f"Current time in {timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif command == 'convert':
            print("Time conversion (format: YYYY-MM-DD HH:MM:SS)")
            time_str = input("Enter time to convert: ").strip()
            from_tz = input("From timezone: ").strip()
            to_tz = input("To timezone: ").strip()
            
            try:
                converted_time = converter.convert_time(time_str, from_tz, to_tz)
                print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif command == 'list':
            choice = input("List (c)ommon timezones or (a)ll timezones? [c/a]: ").lower().strip()
            if choice == 'a':
                print(f"\nAll available timezones ({len(converter.available_zones)} total):")
                print("Note: This is a very long list. Consider using 'search' instead.")
                show_all = input("Show all? [y/N]: ").lower().strip()
                if show_all == 'y':
                    print_timezone_list(converter.available_zones, "All Timezones")
            else:
                print_timezone_list(converter.list_common_timezones(), "Common Timezones")
        
        elif command == 'search':
            search_term = input("Enter search term: ").strip()
            if search_term:
                results = converter.search_timezones(search_term)
                if results:
                    print_timezone_list(results, f"Timezones containing '{search_term}'")
                else:
                    print(f"No timezones found containing '{search_term}'")
        
        else:
            print("Invalid command. Available commands: current, convert, list, search, quit")
    
    print("Thank you for using the Timezone Converter App!")