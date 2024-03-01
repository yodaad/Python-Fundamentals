from statistics import mean

lives = 3
print(type(lives))

age = 39
budget = 1900
temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives += 2
print(lives)

lives -= 1
print(lives)

number_1 = 45000000000000000000.1
number_2 = 0.0000000000000000001
print(number_1)
print(number_2)

jan_budget = 1590
feb_budget = 1288
mar_budget = 2000
total_budget = mean([jan_budget, feb_budget , mar_budget])
print(total_budget)