# Create a dictionary with names and phone numbers
phone_book = {
    "John": "123-456-7890",
    "Mary": "987-654-3210",
    "David": "555-123-4567",
    "Emily": "789-012-3456"
}

# Ask the user for a name
name = input("Enter a name: ")

# Print the phone number of the specified person
if name in phone_book:
    print("Phone number:", phone_book[name])
else:
    print("Name not found in phone book.")
