# Ask the user for 2 numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# Calculate the sum, difference, product, quotient

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"

# Print the results
print(f"The sum is: {sum}")
print(f"The difference is: {difference}")
print(f"The product is: {product}")
print(f"The quotient is: {quotient}")
