# Calculator App

This is a simple calculator application implemented in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division, as well as an RPM (Revolutions Per Minute) calculator.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)
- RPM calculation

## Usage

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, divide, or rpm) and then enter the required numbers for the calculation.

For the RPM calculation, you'll be prompted to enter the distance traveled (in miles) and the time taken (in minutes).

To exit the app, type 'quit' when prompted for an operation.

## Running Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

This will run all the test cases and report the results.

## File Structure

- `calculator.py`: Contains the main Calculator class and the command-line interface.
- `test_calculator.py`: Contains unit tests for the Calculator class.
- `README.md`: This file, containing information about the project.

## License

This project is licensed under the terms of the LICENSE file in the root directory.