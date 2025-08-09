from logger import log_info, log_warning, log_error

class Calculator:
    def add(self, a, b):
        result = a + b
        log_info(f"Addition: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        log_info(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        log_info(f"Multiplication: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            log_error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        result = a / b
        log_info(f"Division: {a} / {b} = {result}")
        return result

def main():
    calc = Calculator()
    log_info("Calculator App started")
    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").lower()
        if operation == 'quit':
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            log_warning(f"Invalid operation attempted: {operation}")
            print("Invalid operation. Please try again.")
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            log_error("Invalid number input")
            print("Invalid input. Please enter valid numbers.")
            continue
        
        try:
            if operation == 'add':
                result = calc.add(a, b)
            elif operation == 'subtract':
                result = calc.subtract(a, b)
            elif operation == 'multiply':
                result = calc.multiply(a, b)
            else:  # divide
                result = calc.divide(a, b)
            
            print(f"Result: {result}")
        except ValueError as e:
            log_error(f"Error during calculation: {str(e)}")
            print(f"Error: {e}")
    
    log_info("Calculator App finished")
    print("Thank you for using the Calculator App!")

if __name__ == "__main__":
    main()