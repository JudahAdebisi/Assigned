import random

print("Welcome to Rock, Paper, Scissors!")
print("-----------------------------------")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nUser: {user_choice}")
    print(f"Computer: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("User wins!")
    else:
        print("Computer wins!")

    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() != "yes":
        break
