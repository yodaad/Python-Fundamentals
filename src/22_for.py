"""
for element in range(1, 21):
    print(element)
"""

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

for person in people:
    print("name =>", person["name"])