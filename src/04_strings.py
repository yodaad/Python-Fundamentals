name = "Diego"
last_name = "Arango"
age = 40

print(name)
print(last_name)

# Concatenation with + operator
full_name = name + " " + last_name
print(full_name)

# Escape character \
quote = 'I\'m Diego'
print(quote)

quote2 = "My favorite book is \"Norwegian Wood\"."
print(quote2)

# Types of formats
template = "Hello, my name is " + name + " and my last name is " + last_name + ". I am " + str(age) + " years old."
print("Template 1:", template)

template2 = "Hello, my name is {} and my last name is {}. I am {} years old.".format(name, last_name, age)
print("Template 2:", template2)

template3 = f"Hello, my name is {name} and my last name is {last_name}. I am {age} years old."
print("Template 3:", template3)