
import re

def check_password_strength(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search("[a-z]", password):
        return False

    # Check if the password contains at least one digit
    if not re.search("[0-9]", password):
        return False

    return True

# Ask the user for a password
password = input("Enter a password: ")

# Check if the password is strong
if check_password_strength(password):
    print("Password is strong")
else:
    print("Password is not strong. Please try again.")
