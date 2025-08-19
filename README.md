# Calculator and BMI Calculator Apps

This repository contains two applications:
1. A simple calculator application implemented in Python.
2. A BMI (Body Mass Index) calculator application implemented in Java.

## Python Calculator App

The Python calculator provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

### Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

### Usage

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

### Running Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

This will run all the test cases and report the results.

## Java BMI Calculator App

The Java BMI calculator allows users to calculate their Body Mass Index based on their weight and height.

### Features

- Calculate BMI based on weight (in kilograms) and height (in meters)
- Provide BMI category (Underweight, Normal weight, Overweight, or Obese)

### Usage

To use the BMI calculator app, compile and run the `BMICalculator.java` file:

```
javac BMICalculator.java
java BMICalculator
```

Follow the on-screen prompts to enter your weight and height. The app will then calculate your BMI and provide the corresponding BMI category.

## File Structure

- `calculator.py`: Contains the main Calculator class and the command-line interface for the Python calculator.
- `test_calculator.py`: Contains unit tests for the Python Calculator class.
- `BMICalculator.java`: Contains the Java implementation of the BMI calculator.
- `README.md`: This file, containing information about the project.

## License

This project is licensed under the terms of the LICENSE file in the root directory.