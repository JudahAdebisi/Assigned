def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", calculate_factorial(num))

