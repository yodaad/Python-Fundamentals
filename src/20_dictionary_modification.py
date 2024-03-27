# Dictionary modification in Python 

person = {
    "name": "Diego",
    "last_name": "Arango",
    "languages": ["Python", "JavaScript"],
    "age": 40
}

print(person)

person["name"] = "Andres"
person["age"] -= 1
person["languages"].append("Java")
print(person)

del person["last_name"]
person.pop("age")
print(person)

person["last_name"] = "Arango"
person["age"] = 40

print("Items")
print(person.items())
print("Keys")
print(person.keys())
print("Values")
print(person.values())