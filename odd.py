# Initialize a variable to store the sum
sum_of_odds = 0

# Loop through all numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is odd
    if num % 2 != 0:
        # Add the number to the sum
        sum_of_odds += num

# Print the sum
print("Sum of odd numbers from 1 to 100:", sum_of_odds)
