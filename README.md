# Session Cookie Management App

This repository contains two applications:
1. A simple calculator application implemented in Python.
2. A session cookie management application using Flask.

## Calculator App

The calculator app provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

### Calculator Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

### Calculator Usage

To use the calculator app, run the `calculator.py` script:

```
python calculator.py
```

Follow the on-screen prompts to perform calculations. Enter the operation you want to perform (add, subtract, multiply, or divide) and then enter the two numbers for the calculation.

To exit the app, type 'quit' when prompted for an operation.

## Session Cookie Management App

The session cookie management app demonstrates how to handle user sessions using cookies in a Flask application.

### Session Management Features

- Create new sessions
- Retrieve session data
- Update session data
- Delete sessions
- Automatic session expiration
- Secure cookie handling

### Session Management Usage

To run the session management app, first install the required dependencies:

```
pip install flask
```

Then, run the `app.py` script:

```
python app.py
```

The app will start a local server, typically at `http://127.0.0.1:5000/`. You can use tools like `curl` or a web browser to interact with the app and test session management.

## Running Tests

To run the unit tests for the calculator, use the following command:

```
python -m unittest test_calculator.py
```

To run the unit tests for the session manager, use the following command:

```
python -m unittest test_session_manager.py
```

To run all tests, use:

```
python -m unittest discover
```

These commands will run all the test cases and report the results.

## File Structure

- `calculator.py`: Contains the main Calculator class and the command-line interface.
- `test_calculator.py`: Contains unit tests for the Calculator class.
- `session_manager.py`: Contains the SessionManager class for handling user sessions.
- `app.py`: Flask application demonstrating the usage of the session manager.
- `test_session_manager.py`: Contains unit tests for the SessionManager class.
- `README.md`: This file, containing information about the project.

## License

This project is licensed under the terms of the LICENSE file in the root directory.