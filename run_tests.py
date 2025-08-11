#!/usr/bin/env python3
"""Test runner script to execute all tests and show results."""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print('='*60)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd='/workspace')
        print("STDOUT:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        print(f"Return code: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def main():
    """Run all tests and show results."""
    print("Testing Timezone Converter Implementation")
    print("=" * 60)
    
    # Test basic import and functionality
    success1 = run_command("python3 test_import.py", "Basic Import and Functionality Test")
    
    # Test calculator (existing functionality)
    success2 = run_command("python3 -m unittest test_calculator.py -v", "Calculator Unit Tests")
    
    # Test timezone converter
    success3 = run_command("python3 -m unittest test_timezone_converter.py -v", "Timezone Converter Unit Tests")
    
    # Test discovery (all tests)
    success4 = run_command("python3 -m unittest discover -v", "All Tests Discovery")
    
    print(f"\n{'='*60}")
    print("SUMMARY:")
    print(f"Basic functionality test: {'PASS' if success1 else 'FAIL'}")
    print(f"Calculator tests: {'PASS' if success2 else 'FAIL'}")
    print(f"Timezone converter tests: {'PASS' if success3 else 'FAIL'}")
    print(f"All tests discovery: {'PASS' if success4 else 'FAIL'}")
    print('='*60)
    
    if all([success1, success2, success3, success4]):
        print("🎉 ALL TESTS PASSED!")
        return 0
    else:
        print("❌ SOME TESTS FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())