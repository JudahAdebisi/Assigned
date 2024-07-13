# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Loop through each digit in the number
while num > 0:
    # Extract the last digit
    digit = num % 10
    # Add the digit to the sum
    sum_of_digits += digit
    # Remove the last digit from the number
    num = num // 10

# Print the sum of digits
print("Sum of digits:", sum_of_digits)
