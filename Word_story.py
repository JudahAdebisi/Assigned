print("Welcome to the Word Story Generator!")
print("------------------------------------------------")

# Ask the user for words
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
place = input("Enter a place: ")

# Generate the story
story = f"One day, a very {adjective} {noun} was walking down the street. " \
        f"The {noun} was {verb} {adverb} towards the {place}. " \
        f"When it arrived, it found a {adjective} surprise waiting for it!"

# Print the story
print("\nHere is your funny story:")
print(story)

