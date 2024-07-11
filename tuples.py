# Create a list of tuples with names and ages
people = [
    ("John", 25),
    ("Mary", 31),
    ("David", 42),
    ("Emily", 28),
    ("Michael", 35)
]

# Print the names of people older than 30
for person in people:
    if person[1] > 30:
        print(person[0])
