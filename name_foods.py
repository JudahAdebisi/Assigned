# Create a dictionary with names and fevorite foods
favorite_foods = {
        "Alice": "Pizza",
        "Bob": "Pineapple",
        "Alex": "Shushi",
        "Judah": "Rice"
}
# Ask the user for a name
name = input("Enter a name: ")

# Check if the name is in the dictionary
if name in favorite_foods:
    # Print outh the favorite food of the specified person
    print(favorite_foods[name])
else:
    print("Name not found in the dictionary")
