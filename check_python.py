#!/usr/bin/env python3
"""Check Python version and available timezone libraries."""

import sys
print(f"Python version: {sys.version}")

# Check for zoneinfo
try:
    from zoneinfo import ZoneInfo, available_timezones
    print("✓ zoneinfo is available (Python 3.9+)")
    print(f"  Sample timezones: {list(available_timezones())[:5]}")
except ImportError:
    print("✗ zoneinfo not available")

# Check for pytz
try:
    import pytz
    print("✓ pytz is available")
    print(f"  Sample timezones: {list(pytz.all_timezones)[:5]}")
except ImportError:
    print("✗ pytz not available")

# Check datetime
try:
    from datetime import datetime
    print(f"✓ datetime available, current time: {datetime.now()}")
except ImportError:
    print("✗ datetime not available")