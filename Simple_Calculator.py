print("Welcome to the Simple Calculator!")
print("-----------------------------------")

while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            continue
    else:
        print("Error: Invalid operator!")
        continue

    print(f"\nThe result is: {result}")

    again = input("\nCalculate again? (yes/no): ")
    if again.lower() != "yes":
        break
