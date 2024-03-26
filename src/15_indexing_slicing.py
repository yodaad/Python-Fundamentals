# Indexing, is the way to access the elements of a sequence like a string, list, tuple, etc.
text = "I am reviewing Python"
print(text[3])
print(text[1])
print(text[len(text) - 1])

# Negative indexing, is the way to access the elements of a sequence like a string, list, tuple, etc. starting from the end. In this example, we are accessing the last element of the text.
print(text[-1])

# Slicing. is the way to access a range of elements of a sequence like a string, list, tuple, etc.
# In this example, we are accessing the first 12 elements of the text.
print(text[0:12])
print(text[:12])

# In this example, we are accessing the elements from the 7th element to the end of the text.
print(text[7:])

# In this example, we are accesing all the elements of the text.
print(text[:])

# In thi example, we are accessing the elements from the 0th element to the 15th element, but we are skipping 1 element.
print(text[0:15:1])

# In this example, we are accessing the elements from the 0th element to the 15th element, but we are skipping 2 elements.
print(text[0:15:2])

# In this example, we are accessing all the elements of the text, but we are skipping 2 elements.
print(text[::2])
