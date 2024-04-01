# Nested loops are loops inside loops. They are used to iterate over items in a list of lists or a list of tuples.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [0] => [1, 2, 3]
print(matrix[0])
# [0][1] => 2
print(matrix[0][1])

# The first loop iterates over the rows of the matrix
for row in matrix:
    print(row)
# The second loop iterates over the columns of the matrix
    for column in row:
        print(column)