# Create - Read - Update - Delete (CRUD) operations are common in programming. In this case, we will see how to perform these operations with lists.

list = [1, 2, 3, 4, 5, 6]
print(list[1])

list[-1] = 10
print(list)

# Append method adds an element to the end of the list.
list.append(700)
print(list)

# Insert method adds an element to the specified index.
list.insert(1, "Hello")
print(list)

# + operator can be used to concatenate two lists.
tasks = ["To do 1", "To do 2", "To do 3"]
new_list = list + tasks
print(new_list)


index = new_list.index("To do 2")
new_list[index] = "To do changed"
print(new_list)

# Remove method removes the first occurrence of the specified value.
new_list.remove("To do 1")
print(new_list)

# Pop method removes the element at the specified index. If the index is not specified, the last element is removed.
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

# Reverse method reverses the order of the list.
new_list.reverse()
print(new_list)

# Sort method sorts the list.
numbers = [1, 4, 6, 3, 7]
numbers.sort()
print(numbers)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)