# Comparison of floating point numbers
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# String representation, not mathematically 
y_str = format(y, ".2g")
print("String =>", y_str)
print(y_str == str(x))

print("-" * 25)

# To deal with such precision issues, it's better to compare floating-point numbers with a certain tolerance
tolerance = 1e-9
print(abs(x - y) < tolerance)

print("-" * 25)

# Another way to compare floating-point numbers is to round them to a certain number of decimal places
print(round(y, 1) == x)