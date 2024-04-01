"""
Range function in Python is used to generate a sequence of numbers. 
The first parameter is the starting point, the second parameter is the ending point, and the third parameter is the step.
"""

my_range = range(1, 5)
for i in my_range:
    print(i)
print(id(my_range))
print("-"*15)

my_range = range(0, 7, 2)
for i in my_range:
    print(i)
print(id(my_range))
print("-"*15)

for i in range(0, 101, 2):
    print(i)

for i in range(0, 100):
    if (i % 2) != 0:
        print(i)
        
for i in range(1, 100, 2):
    print(i)
