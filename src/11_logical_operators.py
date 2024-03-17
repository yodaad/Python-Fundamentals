# AND Operator (&&). It returns True if both conditions are True, otherwise it returns False.
print("AND")
print("True and True =>" , True and True)
print("True and False =>" , True and False)
print("False and True =>" , False and True)
print("False and False =>" , False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = int(input("Enter the amount of items in the stock: "))
print(stock >= 100 and stock <= 1000)

print("-" * 25)

# OR Operator (||). It returns True if at least one of the conditions is True, otherwise it returns False.
print("OR")
print("True or True =>" , True or True)
print("True or False =>" , True or False)
print("False or True =>" , False or True)
print("False or False =>" , False or False)

role = input("Enter the role: ")
print(role == "admin" or role == "sales")
