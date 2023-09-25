import os

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    elif operation == "div":
        return num1 / num2
    else:
        return "Invalid operations"

# Get input values from environment variables
num1 = float(os.environ.get('num1', 0))  # Default value is 0
num2 = float(os.environ.get('num2', 1))  # Default value is 1 to avoid division by zero
operation = os.environ.get('operation', 'add')  # Default operation is 'add'

result = perform_operation(num1, num2, operation)
print("Result is", result)
