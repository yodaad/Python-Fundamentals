if True:
    print("It must execute since the condition is true")

if False:
    print("It will not get executed since the condition is false")

print("-" * 25)

num1 = 10
num2 = 12

if num1 > num2: 
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num2} is greater than {num1}")
    
print("-" * 25)
  
pet = input("What's your favorite pet? ")

if pet == "dog":
    print("Great taste!")
elif pet == "cat":
    print("Nice one!")
elif pet == "fish":
    print("You are so cool!")
else:
    print("You are not that cool...")


"""
stock = int(input("Enter the amount: "))
if stock >= 100 and stock <= 1000:
    print("The stock is within the correct range.")
else:
    print("The amount is not correct!")
"""

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")