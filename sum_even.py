
# Initialize the sum to 0
total = 0

# Loop through all numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is even
    if num % 2 == 0:
        # Add the number to the sum
        total += num

# Print the sum
print("The sum of all even numbers from 1 to 100 is:", total)
