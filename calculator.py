"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 2))
print(calc.subtract(7.5, 2.3))
print(calc.multiply(4, 6.2))

print(Calculator().add(2,10))
