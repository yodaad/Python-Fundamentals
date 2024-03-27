"""
Dictionaries are a collection of key-value pairs. They are unordered, changeable and indexed. They are written with curly brackets and have keys and values separated by a colon. 
The keys must be unique and immutable. The values can be of any data type. You can access the values by using the key name. You can also use the get() method to access the values. 
You can change the values by using the key name. You can loop through the dictionary using a for loop. You can also use the in keyword to check if a key exists in the dictionary. 
You can also use the len() function to get the number of key-value pairs in the dictionary.
"""

my_dictionary = {
    "name": "Diego",
    "last_name": "Arango",
    "age": 39
}

print(my_dictionary)
print(len(my_dictionary))

# Accessing values in a dictionary using the key name.
print(my_dictionary["age"])
print(my_dictionary["last_name"])

# Accessing values in a dictionary using the get() method.
print(my_dictionary.get("age"))
print(my_dictionary.get("height"))

# In returns a boolean value if the key exists in the dictionary.
print("age" in my_dictionary)
print("height" in my_dictionary)
