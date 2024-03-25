# Strings advanced, in Python, are objects that have a lot of methods that can be used to manipulate the text. In this file, we will see some of the most used methods in Python.

text = "She knows how to program in Python."

# in operator, it is used to check if a word is in a text.
print("JavaScript" in text)
print("Python" in text)

word = input("Enter the word that you'd like to search in the text: ")

if word in text:
    print(f"The word {word} was found in the text")
else:
    print(f"The word {word} was not found in the text")

print("-" * 25)

# find method, it is used to find a word in a text. It returns the index of the word in the text. If the word is not found, it returns -1. 
word_2 = input("Enter another word that you'd like to search in the text: ")

if word_2.find(word_2) != -1:
    print(f"The word {word_2} was found in the text")
else:
    print(f"The word {word_2} was not found in the text")

    
print("-" * 25)

# len function, it is used to get the length of a text.
size = len(text)
print(size)

print(text) 
# upper method, it is used to convert the text to uppercase.
print(text.upper())

# lower method, it is used to convert the text to lowercase.
print(text.lower())

# count method, it is used to count the number of times a string appears in a text.
print(text.count("y"))
print(text.lower().count("p"))
# swapcase method, it is used to swap the case of the text.
print(text.swapcase())

# starts with method, it is used to check if a text starts with a specific word.
print(text.startswith("She"))

# endswith method, it is used to check if a text ends with a specific word.
print(text.endswith("Rust"))

# replace method, it is used to replace a word in a text.
print(text.replace("Python", "Java"))

text_2 = "this is just a title."
print(text_2)

# capitalize method, it is used to capitalize the first letter of the text.
print(text_2.capitalize())

# title method, it is used to capitalize the first letter of each word in the text.
print(text_2.title())

# isdigit method, it is used to check if the text is a number.
print(text_2.isdigit())
print("512".isdigit())
