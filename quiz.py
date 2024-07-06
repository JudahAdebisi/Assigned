
print("Welcome to the Quiz!")
print("-------------------------------")

score = 0

# Question 1
question1 = input("What is the capital of France? ")
if question1.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 2
question2 = input("What is 2 + 2? ")
if question2 == "4":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 3
question3 = input("What is the largest planet in our solar system? ")
if question3.lower() == "jupiter":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"\nYour final score is {score} out of 3")
