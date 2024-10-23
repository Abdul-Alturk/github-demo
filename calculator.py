def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    try:
        operation = input("Enter operation (+ or -): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = add(num1, num2)
            print(f"The result of adding {num1} and {num2} is {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"The result of subtracting {num2} from {num1} is {result}")
        else:
            print("Invalid operation. Please enter + or -.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")