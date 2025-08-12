#!/usr/bin/env python3
"""
Final validation script for the String Case Converter App
"""

import unittest
import sys

def validate_implementation():
    """Validate the complete implementation"""
    print("Validating String Case Converter Implementation...")
    print("=" * 50)
    
    success = True
    
    # Test 1: Import modules
    try:
        from string_case_converter import StringCaseConverter
        from calculator import Calculator
        print("✓ All modules import successfully")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        success = False
    
    # Test 2: Basic functionality
    try:
        converter = StringCaseConverter()
        
        # Test each conversion method
        test_cases = [
            (converter.to_camel_case("hello world"), "helloWorld"),
            (converter.to_pascal_case("hello world"), "HelloWorld"),
            (converter.to_snake_case("helloWorld"), "hello_world"),
            (converter.to_kebab_case("HelloWorld"), "hello-world"),
            (converter.to_uppercase("hello"), "HELLO"),
            (converter.to_lowercase("HELLO"), "hello"),
            (converter.to_title_case("hello world"), "Hello World"),
            (converter.to_alternating_case("hello"), "hElLo"),
            (converter.to_sentence_case("hello world"), "Hello world"),
        ]
        
        for result, expected in test_cases:
            if result != expected:
                print(f"✗ Expected '{expected}', got '{result}'")
                success = False
        
        if success:
            print("✓ All conversion methods work correctly")
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")
        success = False
    
    # Test 3: Unit tests
    try:
        from test_string_case_converter import TestStringCaseConverter
        suite = unittest.TestLoader().loadTestsFromTestCase(TestStringCaseConverter)
        runner = unittest.TextTestRunner(verbosity=0, stream=open('/dev/null', 'w'))
        result = runner.run(suite)
        
        if result.wasSuccessful():
            print(f"✓ All {result.testsRun} unit tests pass")
        else:
            print(f"✗ {len(result.failures + result.errors)} unit tests failed")
            success = False
    except Exception as e:
        print(f"✗ Unit test validation failed: {e}")
        success = False
    
    # Test 4: Edge cases
    try:
        converter = StringCaseConverter()
        edge_cases = [
            (converter.to_camel_case(""), ""),
            (converter.to_pascal_case("a"), "A"),
            (converter.to_snake_case("XMLHttpRequest"), "xml_http_request"),
            (converter.to_kebab_case("hello@world#test"), "hello-world-test"),
        ]
        
        for result, expected in edge_cases:
            if result != expected:
                print(f"✗ Edge case failed: expected '{expected}', got '{result}'")
                success = False
        
        if success:
            print("✓ Edge cases handled correctly")
    except Exception as e:
        print(f"✗ Edge case test failed: {e}")
        success = False
    
    print("=" * 50)
    if success:
        print("🎉 VALIDATION SUCCESSFUL!")
        print("\nThe String Case Converter App is ready to use:")
        print("  • Run: python string_case_converter.py")
        print("  • Test: python -m unittest test_string_case_converter.py")
        print("  • Demo: python demo.py")
    else:
        print("❌ VALIDATION FAILED!")
        print("Please check the errors above.")
    
    return success

if __name__ == "__main__":
    success = validate_implementation()
    sys.exit(0 if success else 1)