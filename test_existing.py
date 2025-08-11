#!/usr/bin/env python3
"""Test existing calculator functionality to ensure we didn't break anything."""

import unittest
import sys

def test_calculator_manually():
    """Manual test of calculator functionality."""
    print("Manual Calculator Test")
    print("-" * 30)
    
    try:
        from calculator import Calculator
        calc = Calculator()
        
        # Test basic operations
        assert calc.add(2, 3) == 5, "Addition failed"
        print("✓ Addition: 2 + 3 = 5")
        
        assert calc.subtract(5, 3) == 2, "Subtraction failed"
        print("✓ Subtraction: 5 - 3 = 2")
        
        assert calc.multiply(4, 3) == 12, "Multiplication failed"
        print("✓ Multiplication: 4 * 3 = 12")
        
        assert calc.divide(10, 2) == 5, "Division failed"
        print("✓ Division: 10 / 2 = 5")
        
        # Test division by zero
        try:
            calc.divide(5, 0)
            assert False, "Division by zero should raise ValueError"
        except ValueError:
            print("✓ Division by zero properly raises ValueError")
        
        print("✓ All calculator tests passed!")
        return True
        
    except Exception as e:
        print(f"✗ Calculator test failed: {e}")
        return False

def run_calculator_unit_tests():
    """Run the actual calculator unit tests."""
    print("\nCalculator Unit Tests")
    print("-" * 30)
    
    try:
        # Import and run calculator tests
        from test_calculator import TestCalculator
        
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        success = result.wasSuccessful()
        print(f"\nUnit tests: {'PASSED' if success else 'FAILED'}")
        
        if not success:
            print("Failures:")
            for test, error in result.failures:
                print(f"  {test}: {error}")
            print("Errors:")
            for test, error in result.errors:
                print(f"  {test}: {error}")
        
        return success
        
    except Exception as e:
        print(f"✗ Unit test execution failed: {e}")
        return False

def main():
    """Run all calculator tests."""
    print("CALCULATOR FUNCTIONALITY TEST")
    print("=" * 40)
    
    manual_success = test_calculator_manually()
    unit_success = run_calculator_unit_tests()
    
    print("\n" + "=" * 40)
    print("RESULTS:")
    print(f"Manual tests: {'PASS' if manual_success else 'FAIL'}")
    print(f"Unit tests: {'PASS' if unit_success else 'FAIL'}")
    print("=" * 40)
    
    if manual_success and unit_success:
        print("🎉 Calculator is working perfectly!")
        return 0
    else:
        print("❌ Calculator has issues!")
        return 1

if __name__ == "__main__":
    sys.exit(main())