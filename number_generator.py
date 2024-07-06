import random

# Choose a random number between 1 and 100
number_to_guess = random.randint(1, 100)

while True:
    # Ask the user for their guess
    user_guess = int(input("Guess a number between 1 and 100: "))

    # Check if the user's guess is correct
    if user_guess == number_to_guess:
        print("Congratulations! You've guessed the number correctly.")
        break

    # Print "Too high" or "Too low" depending on the user's guess
    elif user_guess > number_to_guess:
        print("Too high. Try again!")
    else:
        print("Too low. Try again!")
