# Dictionary modification in Python 

person = {
    "name": "Diego",
    "last_name": "Arango",
    "languages": ["Python", "JavaScript"],
    "age": 40
}

print(person)

# Modify values in a dictionary
person["name"] = "Andres"
person["age"] -= 1
person["languages"].append("Java")
print(person)

# Del removes the key and value from the dictionary
del person["last_name"]

# Pop removes the key and value from the dictionary as well
person.pop("age")
print(person)

# Add a new key-value pair to the dictionary using the key name and the assignment operator
person["last_name"] = "Arango"
person["age"] = 40

# Items returns a list of tuples with key-value pairs
print("Items")
print(person.items())

# Keys returns a list of keys
print("Keys")
print(person.keys())

# Values returns a list of values
print("Values")
print(person.values())

# Copy returns a copy of the dictionary
new_person = person.copy()
print("Copied dictionary: ", new_person)

# Clear removes all key-value pairs from the dictionary
new_person.clear()
print("Cleared dictionary: ", new_person)