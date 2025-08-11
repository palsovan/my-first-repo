# Python Utility Apps

This repository contains two Python utility applications: a Calculator and a Timezone Converter.

## Calculator App

A simple calculator application that provides basic arithmetic operations.

### Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

### Usage

To use the calculator app, run the `calculator.py` script:

```bash
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

## Timezone Converter App

A comprehensive timezone converter application that allows you to convert times between different timezones and get current time in various locations around the world.

### Features

- Convert time from one timezone to another
- Get current time in any timezone
- List common timezones
- Search for timezones by name
- Support for custom time formats
- Handles daylight saving time automatically
- Compatible with Python 3.9+ (using zoneinfo) or older versions with pytz

### Usage

To use the timezone converter app, run the `timezone_converter.py` script:

```bash
python timezone_converter.py
```

Available commands:
- `current`: Get current time in a specific timezone
- `convert`: Convert time from one timezone to another
- `list`: Show common timezones or all available timezones
- `search`: Search for timezones containing a specific term
- `quit`: Exit the application

### Examples

**Get current time:**
```
Enter command: current
Enter timezone (or 'list' to see options): US/Eastern
Current time in US/Eastern: 2023-06-15 14:30:45 EDT
```

**Convert time:**
```
Enter command: convert
Time conversion (format: YYYY-MM-DD HH:MM:SS)
Enter time to convert: 2023-06-15 12:00:00
From timezone: UTC
To timezone: US/Pacific
Converted time: 2023-06-15 05:00:00 PDT
```

**Search timezones:**
```
Enter command: search
Enter search term: Tokyo
Timezones containing 'Tokyo':
1. Asia/Tokyo
```

### Requirements

The timezone converter requires either:
- Python 3.9+ (uses built-in `zoneinfo` module), or
- Python 3.6+ with `pytz` library installed: `pip install pytz`

## Running Tests

To run the unit tests for both applications:

```bash
# Test calculator
python -m unittest test_calculator.py

# Test timezone converter
python -m unittest test_timezone_converter.py

# Run all tests
python -m unittest discover
```

## File Structure

- `calculator.py`: Contains the main Calculator class and CLI interface
- `test_calculator.py`: Contains unit tests for the Calculator class
- `timezone_converter.py`: Contains the main TimezoneConverter class and CLI interface
- `test_timezone_converter.py`: Contains unit tests for the TimezoneConverter class
- `README.md`: This file, containing information about the project
- `LICENSE`: Apache 2.0 license file

## License

This project is licensed under the terms of the Apache 2.0 LICENSE file in the root directory.