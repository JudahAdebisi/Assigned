# Ask the user for a list of numbers
numbers = input("Enter a list of numbers (separated by spaces): ")

# Split the input into a list of numbers
numbers = list(map(int, numbers.split()))

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Print the results
print("Largest number:", largest)
print("Smallest number:", smallest)



