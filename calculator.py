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

    def calculate_speed(self, distance, time):
        if time == 0:
            raise ValueError("Time cannot be zero")
        return self.divide(distance, time)

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide, speed")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").lower()
        if operation == 'quit':
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide', 'speed']:
            print("Invalid operation. Please try again.")
            continue
        
        if operation == 'speed':
            distance = float(input("Enter distance in miles: "))
            time = float(input("Enter time in hours: "))
            try:
                result = calc.calculate_speed(distance, time)
                print(f"Speed: {result} miles per hour")
            except ValueError as e:
                print(f"Error: {e}")
                continue
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