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

if __name__ == "__main__":
    try:
        operation = input("Enter operation (+, -, *, /): ")
        num1 = float(input("Enter first number: "))
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
            print("Invalid operation. Please enter +, -, *, or /.")
    except ValueError as e:
        print(f"Invalid input: {e}")