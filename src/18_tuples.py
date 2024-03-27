# Unlike lists, tuples can not be modified. They are immutable. Tuples are defined with parentheses.

numbers = (1, 2, 3, 5)
strings = ("Dann", "Mary", "John", "Dann")

print(numbers)
print("0: ", numbers[0])
print("-1: ", numbers[-1])
print(type(numbers))
print(strings)
print(type(strings))

# Index and count methods can be used with tuples.
print(strings.index("Mary"))
print(strings.count("Dann"))

# Convert a tuple to a list.
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = "Ivan"
print(my_list)

# Convert a list to a tuple.
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))