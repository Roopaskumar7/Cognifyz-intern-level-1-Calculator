# Basic Calculator Program

# Get input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on the operator
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid operator! Please use one of (+, -, *, /, %)")
