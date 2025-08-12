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

    def pounds_to_kg(self, pounds):
        return pounds * 0.45359237

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide, weight")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").lower()
        if operation == 'quit':
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide', 'weight']:
            print("Invalid operation. Please try again.")
            continue
        
        if operation == 'weight':
            pounds = float(input("Enter weight in pounds: "))
            result = calc.pounds_to_kg(pounds)
            print(f"{pounds} pounds is equal to {result:.2f} kilograms")
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