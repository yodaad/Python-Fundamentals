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

size = len(text)
print(size)

print(text) 
print(text.upper())
print(text.lower())
print(text.count("y"))
print(text.lower().count("p"))
print(text.swapcase())
print(text.startswith("She"))
print(text.endswith("Rust"))
print(text.replace("Python", "Java"))

text_2 = "this is just a title."
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("512".isdigit())
