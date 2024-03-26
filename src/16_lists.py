# Lists are a collection of items that are ordered and changeable. Allows duplicate members. Allows different data types.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers)
print(type(numbers))

tasks = ["Check modules", "Update Trello", "Manage personal responsabilities"]
print(tasks)

types = [1, True, "Hello"]
print(types)

print(numbers[0])
print(tasks[1])

tasks[0] = "Check functions"
print(tasks)

tasks[0] = "Check modules again"
print(tasks)

print(numbers[:4])
print(1 in types)
numbers.reverse()
print(numbers)

