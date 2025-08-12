class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def calculate_rpm(self, distance, time):
        if time == 0:
            raise ValueError("Time cannot be zero")
        return (distance / time) * 60

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide, rpm")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").lower()
        if operation == 'quit':
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide', 'rpm']:
            print("Invalid operation. Please try again.")
            continue
        
        if operation == 'rpm':
            distance = float(input("Enter distance traveled (in miles): "))
            time = float(input("Enter time taken (in minutes): "))
            try:
                result = calc.calculate_rpm(distance, time)
                print(f"RPM (Revolutions Per Minute): {result:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if operation == 'add':
                result = calc.add(a, b)
            elif operation == 'subtract':
                result = calc.subtract(a, b)
            elif operation == 'multiply':
                result = calc.multiply(a, b)
            else:  # divide
                try:
                    result = calc.divide(a, b)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
            
            print(f"Result: {result}")
    
    print("Thank you for using the Calculator App!")