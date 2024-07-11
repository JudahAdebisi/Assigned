numbers = input("Enter a list of numbers: ").split()
numbers = [int(num) for num in numbers]
total = sum(numbers)
average = total / len(numbers)
print("Average:", average)
