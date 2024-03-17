# NOT Operator (!). It returns True if the condition is False, otherwise it returns False.
print(not True)
print(not False)

print("-" * 25)

# NOT AND Operator. It returns True if at least one of the conditions is False, otherwise it returns False.
print("NOT AND")
print("Not True and Not True =>" , not (True and True))
print("Not True and Not False =>" , not (True and False))
print("Not False and Not True =>" , not (False and True))
print("Not False and Not False =>" , not (False and False))

print("-" * 25)

stock = int(input("Enter the amount of items in the stock: "))
print(not (stock >= 100 and stock <= 1000))

print("-" * 25)

# NOT OR Operator. It returns True if both conditions are False, otherwise it returns False.
print("NOT OR")
print("Not True or Not True =>" , not (True or True))
print("Not True or Not False =>" , not (True or False))
print("Not False or Not True =>" , not (False or True))
print("Not False or Not False =>" , not (False or False))

