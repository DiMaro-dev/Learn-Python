# Basic Calculator 
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

# input first number
while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# input second number
while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# input operation
while True:
    operation = input("Enter operation (+, -, *, /): ")
    if operation in ('+', '-', '*', '/'):
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Perform the operation based on user input
match operation:  # Using match-case for operation selection
    case '+':   
        result = num1 + num2  # Addition    
    case '-':
        result = num1 - num2  # Subtraction 
    case '*':               
        result = num1 * num2  # Multiplication
    case '/':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2  # Division
        else:
            result = "Error! Division by zero."
    case _:
        result = "Invalid operation!"  # Handle invalid operation
print("Result:", result)  # Output the result
