# Inputs
num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())
operation = input("Enter the arithmetic operation (+, -, *, /, %): ").strip()

# Perform the arithmetic operation based on the numbers and operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "%":
    result = num1 % num2
else:
    result = None

# Output
if result is not None:
    print(f"Example One {num1} {operation} {num2} = {result}")
    print(f"Example Two {num1} {operation} {num2} = {result}")
else:
    print("Invalid operation")