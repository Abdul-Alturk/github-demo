import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def root(a, b):
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot take even root of a negative number.")
    return a ** (1 / b)

if __name__ == "__main__":
    try:
        operation = input("Enter operation (+, -, *, /, root): ")
        num1 = float(input("Enter first number: "))
        
        if operation == 'root':
            num2 = float(input("Enter the root degree: "))
            result = root(num1, num2)
            print(f"The {num2}-th root of {num1} is {result}")
        else:
            num2 = float(input("Enter second number: "))
            if operation == '+':
                result = add(num1, num2)
                print(f"The result of adding {num1} and {num2} is {result}")
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"The result of subtracting {num2} from {num1} is {result}")
            elif operation == '*':
                result = multiply(num1, num2)
                print(f"The result of multiplying {num1} and {num2} is {result}")
            elif operation == '/':
                result = divide(num1, num2)
                print(f"The result of dividing {num1} by {num2} is {result}")
            else:
                print("Invalid operation. Please enter +, -, *, /, or root.")
    except ValueError as e:
        print(f"Invalid input: {e}")