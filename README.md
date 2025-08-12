# Python Utility Apps

This repository contains two Python utility applications:

## Calculator App

A simple calculator application that provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

## String Case Converter App

A comprehensive string case converter that supports multiple case conversion formats including camelCase, PascalCase, snake_case, kebab-case, and more.

## Calculator Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## String Case Converter Features

- **lowercase**: Convert text to all lowercase
- **UPPERCASE**: Convert text to all uppercase
- **Title Case**: Convert text to title case (first letter of each word capitalized)
- **camelCase**: Convert text to camelCase (first word lowercase, subsequent words capitalized, no spaces)
- **PascalCase**: Convert text to PascalCase (all words capitalized, no spaces)
- **snake_case**: Convert text to snake_case (lowercase with underscores)
- **kebab-case**: Convert text to kebab-case (lowercase with hyphens)
- **aLtErNaTiNg CaSe**: Convert text to alternating case
- **Sentence case**: Convert text to sentence case (first letter capitalized, rest lowercase)

## Usage

### Calculator App

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

### String Case Converter App

To use the string case converter app, run the `string_case_converter.py` script:

```
python string_case_converter.py
```

Follow the on-screen prompts to convert text. Enter the conversion type you want to perform (lowercase, uppercase, title, camel, pascal, snake, kebab, alternating, or sentence) and then enter the text you want to convert.

To exit the app, type 'quit' when prompted for a conversion type.

## Running Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

To run the unit tests for the string case converter, use the following command:

```
python -m unittest test_string_case_converter.py
```

To run all tests at once, use:

```
python -m unittest discover
```

This will run all the test cases and report the results.

## File Structure

- `calculator.py`: Contains the main Calculator class and the command-line interface.
- `test_calculator.py`: Contains unit tests for the Calculator class.
- `string_case_converter.py`: Contains the main StringCaseConverter class and the command-line interface.
- `test_string_case_converter.py`: Contains unit tests for the StringCaseConverter class.
- `README.md`: This file, containing information about the project.
- `LICENSE`: Apache 2.0 license file.

## License

This project is licensed under the terms of the LICENSE file in the root directory.