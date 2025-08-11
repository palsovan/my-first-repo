# Calculator and UUID Generator App

This repository contains two applications implemented in Python:
1. A simple calculator that provides basic arithmetic operations.
2. A UUID generator that creates unique identifiers with logging functionality.

## Features

### Calculator
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

### UUID Generator
- Generates UUID version 4 (random)
- Logs each UUID generation with timestamp

## Usage

### Calculator

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

### UUID Generator

To use the UUID generator, run the `uuid_generator.py` script:

```
python uuid_generator.py
```

This will generate and display a new UUID. The generation will also be logged with a timestamp.

## Running Tests

### Calculator Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

### UUID Generator Tests

To run the unit tests for the UUID generator, use the following command:

```
python -m unittest test_uuid_generator.py
```

These commands will run all the test cases for each application and report the results.

## File Structure

- `calculator.py`: Contains the main Calculator class and the command-line interface.
- `test_calculator.py`: Contains unit tests for the Calculator class.
- `uuid_generator.py`: Contains the UUID generator functionality with logging.
- `test_uuid_generator.py`: Contains unit tests for the UUID generator.
- `README.md`: This file, containing information about the project.

## License

This project is licensed under the terms of the LICENSE file in the root directory.