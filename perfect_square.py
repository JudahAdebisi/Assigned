import math

def is_perfect_square(n):
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")

