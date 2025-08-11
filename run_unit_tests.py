#!/usr/bin/env python3
"""Run unit tests and show detailed results."""

import unittest
import sys
import io
from contextlib import redirect_stdout, redirect_stderr

def run_test_module(module_name, description):
    """Run a specific test module and capture results."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print('='*60)
    
    try:
        # Import the test module
        test_module = __import__(module_name)
        
        # Create test suite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)
        
        # Run tests with detailed output
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)
        
        # Print results
        output = stream.getvalue()
        print(output)
        
        # Summary
        print(f"\nSUMMARY for {description}:")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
        
        if result.failures:
            print("\nFAILURES:")
            for test, traceback in result.failures:
                print(f"- {test}: {traceback}")
        
        if result.errors:
            print("\nERRORS:")
            for test, traceback in result.errors:
                print(f"- {test}: {traceback}")
        
        return result.wasSuccessful()
        
    except Exception as e:
        print(f"Error running {module_name}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all unit tests."""
    print("UNIT TEST EXECUTION")
    print("=" * 60)
    
    # Test calculator
    calc_success = run_test_module('test_calculator', 'Calculator Unit Tests')
    
    # Test timezone converter
    tz_success = run_test_module('test_timezone_converter', 'Timezone Converter Unit Tests')
    
    print(f"\n{'='*60}")
    print("FINAL SUMMARY:")
    print(f"Calculator tests: {'PASS' if calc_success else 'FAIL'}")
    print(f"Timezone converter tests: {'PASS' if tz_success else 'FAIL'}")
    print('='*60)
    
    if calc_success and tz_success:
        print("🎉 ALL UNIT TESTS PASSED!")
        return 0
    else:
        print("❌ SOME UNIT TESTS FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())