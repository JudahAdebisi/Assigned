print("Welcome to the Fibonacci Numbers")
print("---------------------------------------")

# The first two Fibonacci numbers
a, b = 0, 1

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
