#!/usr/bin/env python3
"""
Demonstration of the String Case Converter App
"""

from string_case_converter import StringCaseConverter

def main():
    print("=" * 60)
    print("STRING CASE CONVERTER DEMONSTRATION")
    print("=" * 60)
    
    converter = StringCaseConverter()
    
    # Test cases with different types of input
    test_cases = [
        "hello world",
        "Hello World",
        "helloWorld",
        "HelloWorld", 
        "hello_world",
        "hello-world",
        "THE QUICK BROWN FOX",
        "XMLHttpRequest",
        "iPhone App Store",
        "user_name_field",
        "background-color",
        "JavaScript",
    ]
    
    for test_input in test_cases:
        print(f"\nInput: '{test_input}'")
        print("-" * 40)
        
        conversions = [
            ("Lowercase", converter.to_lowercase(test_input)),
            ("Uppercase", converter.to_uppercase(test_input)),
            ("Title Case", converter.to_title_case(test_input)),
            ("Sentence Case", converter.to_sentence_case(test_input)),
            ("camelCase", converter.to_camel_case(test_input)),
            ("PascalCase", converter.to_pascal_case(test_input)),
            ("snake_case", converter.to_snake_case(test_input)),
            ("kebab-case", converter.to_kebab_case(test_input)),
            ("aLtErNaTiNg", converter.to_alternating_case(test_input)),
        ]
        
        for name, result in conversions:
            print(f"  {name:12}: '{result}'")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nTo use the interactive version, run:")
    print("  python string_case_converter.py")
    print("\nTo run tests, use:")
    print("  python -m unittest test_string_case_converter.py")

if __name__ == "__main__":
    main()