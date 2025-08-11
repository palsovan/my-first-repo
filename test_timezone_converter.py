import unittest
from datetime import datetime
from timezone_converter import TimezoneConverter
import sys

# Check if we're using zoneinfo or pytz
try:
    from zoneinfo import ZoneInfo
    USE_ZONEINFO = True
except ImportError:
    try:
        import pytz
        USE_ZONEINFO = False
    except ImportError:
        USE_ZONEINFO = None


class TestTimezoneConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TimezoneConverter()
    
    def test_initialization(self):
        """Test that the converter initializes properly."""
        self.assertIsInstance(self.converter, TimezoneConverter)
        self.assertIsInstance(self.converter.available_zones, list)
        self.assertGreater(len(self.converter.available_zones), 0)
    
    def test_validate_timezone(self):
        """Test timezone validation."""
        # Test valid timezones
        self.assertTrue(self.converter.validate_timezone('UTC'))
        self.assertTrue(self.converter.validate_timezone('US/Eastern'))
        
        # Test invalid timezone
        self.assertFalse(self.converter.validate_timezone('Invalid/Timezone'))
        self.assertFalse(self.converter.validate_timezone(''))
    
    def test_get_current_time(self):
        """Test getting current time in different timezones."""
        # Test UTC
        utc_time = self.converter.get_current_time('UTC')
        self.assertIsInstance(utc_time, datetime)
        
        # Test US/Eastern
        if 'US/Eastern' in self.converter.available_zones:
            eastern_time = self.converter.get_current_time('US/Eastern')
            self.assertIsInstance(eastern_time, datetime)
        
        # Test invalid timezone
        with self.assertRaises(ValueError):
            self.converter.get_current_time('Invalid/Timezone')
    
    def test_convert_time_basic(self):
        """Test basic time conversion functionality."""
        # Test UTC to US/Eastern conversion
        if 'US/Eastern' in self.converter.available_zones:
            result = self.converter.convert_time(
                '2023-06-15 12:00:00', 
                'UTC', 
                'US/Eastern'
            )
            self.assertIsInstance(result, datetime)
            # In June, Eastern time should be UTC-4 (EDT)
            # So 12:00 UTC should be 08:00 EDT
            self.assertEqual(result.hour, 8)
    
    def test_convert_time_same_timezone(self):
        """Test converting time within the same timezone."""
        result = self.converter.convert_time(
            '2023-06-15 12:00:00',
            'UTC',
            'UTC'
        )
        self.assertEqual(result.hour, 12)
        self.assertEqual(result.day, 15)
    
    def test_convert_time_invalid_format(self):
        """Test conversion with invalid time format."""
        with self.assertRaises(ValueError) as context:
            self.converter.convert_time(
                'invalid-time-format',
                'UTC',
                'US/Eastern'
            )
        self.assertIn('Invalid time format', str(context.exception))
    
    def test_convert_time_invalid_timezone(self):
        """Test conversion with invalid timezone."""
        with self.assertRaises(ValueError):
            self.converter.convert_time(
                '2023-06-15 12:00:00',
                'Invalid/Timezone',
                'UTC'
            )
        
        with self.assertRaises(ValueError):
            self.converter.convert_time(
                '2023-06-15 12:00:00',
                'UTC',
                'Invalid/Timezone'
            )
    
    def test_list_common_timezones(self):
        """Test listing common timezones."""
        common_zones = self.converter.list_common_timezones()
        self.assertIsInstance(common_zones, list)
        self.assertGreater(len(common_zones), 0)
        
        # UTC should always be available
        self.assertIn('UTC', common_zones)
        
        # All returned zones should be valid
        for zone in common_zones:
            self.assertTrue(self.converter.validate_timezone(zone))
    
    def test_search_timezones(self):
        """Test timezone search functionality."""
        # Search for US timezones
        us_zones = self.converter.search_timezones('US')
        self.assertIsInstance(us_zones, list)
        
        # All results should contain 'US' (case insensitive)
        for zone in us_zones:
            self.assertIn('US', zone.upper())
        
        # Search for Europe timezones
        europe_zones = self.converter.search_timezones('Europe')
        self.assertIsInstance(europe_zones, list)
        
        # Search for non-existent timezone
        empty_results = self.converter.search_timezones('NonExistentPlace')
        self.assertEqual(len(empty_results), 0)
    
    def test_search_timezones_case_insensitive(self):
        """Test that timezone search is case insensitive."""
        results_lower = self.converter.search_timezones('america')
        results_upper = self.converter.search_timezones('AMERICA')
        results_mixed = self.converter.search_timezones('America')
        
        # All should return the same results
        self.assertEqual(results_lower, results_upper)
        self.assertEqual(results_lower, results_mixed)
    
    def test_convert_time_custom_format(self):
        """Test time conversion with custom time format."""
        # Test with different time format
        custom_format = "%d/%m/%Y %H:%M"
        if 'US/Pacific' in self.converter.available_zones:
            result = self.converter.convert_time(
                '15/06/2023 14:30',
                'UTC',
                'US/Pacific',
                custom_format
            )
            self.assertIsInstance(result, datetime)
            # In June, Pacific time should be UTC-7 (PDT)
            # So 14:30 UTC should be 07:30 PDT
            self.assertEqual(result.hour, 7)
            self.assertEqual(result.minute, 30)
    
    def test_winter_time_conversion(self):
        """Test conversion during winter time (standard time)."""
        # Test conversion in January when daylight saving is not active
        if 'US/Eastern' in self.converter.available_zones:
            result = self.converter.convert_time(
                '2023-01-15 12:00:00',
                'UTC',
                'US/Eastern'
            )
            # In January, Eastern time should be UTC-5 (EST)
            # So 12:00 UTC should be 07:00 EST
            self.assertEqual(result.hour, 7)
    
    def test_cross_date_conversion(self):
        """Test conversion that crosses date boundaries."""
        if 'Asia/Tokyo' in self.converter.available_zones:
            result = self.converter.convert_time(
                '2023-06-15 20:00:00',
                'UTC',
                'Asia/Tokyo'
            )
            # Tokyo is UTC+9, so 20:00 UTC should be 05:00 next day
            self.assertEqual(result.hour, 5)
            self.assertEqual(result.day, 16)  # Next day


class TestTimezoneConverterEdgeCases(unittest.TestCase):
    def setUp(self):
        self.converter = TimezoneConverter()
    
    def test_empty_search_term(self):
        """Test search with empty string."""
        results = self.converter.search_timezones('')
        # Empty search should return all timezones
        self.assertEqual(len(results), len(self.converter.available_zones))
    
    def test_whitespace_handling(self):
        """Test that whitespace in timezone names is handled properly."""
        # Test with leading/trailing spaces
        with self.assertRaises(ValueError):
            self.converter.get_current_time(' UTC ')
    
    def test_leap_year_conversion(self):
        """Test conversion on leap year date."""
        result = self.converter.convert_time(
            '2024-02-29 12:00:00',  # Leap year date
            'UTC',
            'UTC'
        )
        self.assertEqual(result.day, 29)
        self.assertEqual(result.month, 2)


if __name__ == '__main__':
    # Skip tests if neither zoneinfo nor pytz is available
    if USE_ZONEINFO is None:
        print("Skipping tests: Neither zoneinfo nor pytz is available")
        sys.exit(0)
    
    unittest.main()