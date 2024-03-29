# Loop for in Python 

# Range function in Python is used to generate a sequence of numbers. The first parameter is the starting point, the second parameter is the ending point, and the third parameter is the step.
for element in range(1, 21, 2):
    print(element)


# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
my_list = [23, 45, 67,89, 43]

for number in my_list:
    print(number)

my_tuple = ("Diego", "Dann", "Mike")

for names in my_tuple:
    print(names)
    
product = {
    "name": "shirt",
    "price": 100,
    "stock": 89
}

# The for loop can be used to iterate over the keys of a dictionary
for key in product:
    print(key, "=>", product[key])
    
for key, value in product.items():
    print(key, "=>", value)
   
    
people = [
    {
        "name": "Diego",
        "age": 39
    },
    {
        "name": "Dann",
        "age": 45
    },
    {
        "name": "Mike",
        "age": 32
    }
]

# The for loop can be used to iterate over a list of dictionaries
for person in people:
    print("name =>", person["name"])