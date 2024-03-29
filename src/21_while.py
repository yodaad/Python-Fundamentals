# While loop in Python 

counter = 0
while counter < 10:
    counter += 1
    print("Counter:", counter)
    
# Break statement in Python is used to exit the loop immediately 
counter1 = 0
while counter1 < 20:
    counter1 += 1
    if counter1 == 15:
        break
    print("Counter1:",counter1)


# Continue statement in Python is used to skip the current iteration and continue with the next one
counter2 = 0

while counter2 < 20:
    counter2 += 1
    if counter2 < 10:
        continue
    print("Counter2:",counter2)