print("Welcome to the Word Reverser!")
print("-----------------------------------")

sentence = input("Enter a sentence: ")

words = sentence.split()  # split the sentence into words
reversed_words = words[::-1]  # reverse the order of the words

reversed_sentence = " ".join(reversed_words)  # join the words back into a sentence

print(f"\nThe reversed sentence is: {reversed_sentence}")

