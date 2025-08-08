# Calculator App with Redis Caching

This is a simple calculator application implemented in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division, with results cached using Redis for improved performance.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)
- Redis caching for faster repeated calculations

## Requirements

- Python 3.6+
- Redis server
- redis-py library

## Setup

1. Install the required Python packages:

```
pip install -r requirements.txt
```

2. Make sure you have a Redis server running. By default, the app will try to connect to Redis on localhost:6379. You can modify the connection settings in the `Calculator` class initialization if needed.

## Usage

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

## Running Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

This will run all the test cases and report the results.

## File Structure

- `calculator.py`: Contains the main Calculator class with Redis caching and the command-line interface.
- `test_calculator.py`: Contains unit tests for the Calculator class, including tests for Redis caching.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: This file, containing information about the project.

## Redis Caching

The calculator app uses Redis to cache the results of calculations. This means that if you perform the same calculation multiple times, the app will retrieve the result from the cache instead of recalculating it, resulting in faster performance.

The cache keys are structured as follows: `calc:{operation}:{a}:{b}`, where `{operation}` is the arithmetic operation, and `{a}` and `{b}` are the input numbers.

## License

This project is licensed under the terms of the LICENSE file in the root directory.