import redis

class Calculator:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    def _cache_key(self, operation, a, b):
        return f"calc:{operation}:{a}:{b}"

    def _cached_operation(self, operation, a, b):
        key = self._cache_key(operation, a, b)
        cached_result = self.redis_client.get(key)
        if cached_result is not None:
            return float(cached_result)
        
        result = getattr(self, f"_{operation}")(a, b)
        self.redis_client.set(key, str(result))
        return result

    def _add(self, a, b):
        return a + b

    def _subtract(self, a, b):
        return a - b

    def _multiply(self, a, b):
        return a * b

    def _divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def add(self, a, b):
        return self._cached_operation("add", a, b)

    def subtract(self, a, b):
        return self._cached_operation("subtract", a, b)

    def multiply(self, a, b):
        return self._cached_operation("multiply", a, b)

    def divide(self, a, b):
        return self._cached_operation("divide", a, b)

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator App!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        operation = input("Enter operation (or 'quit' to exit): ").lower()
        if operation == 'quit':
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue
        
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        try:
            result = getattr(calc, operation)(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    
    print("Thank you for using the Calculator App!")