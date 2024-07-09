import os
import sys

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
# Ensure correct number of command-line arguments
if len(sys.argv) != 4:
    print("Usage: python app.py <num1> <num2> <operation>")
    sys.exit(1)

# Extract input values from command-line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

result = perform_operation(num1, num2, operation)
print(result)
