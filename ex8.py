matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]
result = []
row_start = 0
row_end = len(matrix)
column_start = 0
column_end = len(matrix[0])
while row_start < row_end and column_start < column_end:

    
    for column in range(column_start, column_end):# Traverse from left to right
        result.append(matrix[row_start][column])
    row_start = row_start + 1

    
    for row in range(row_start, row_end):# Traverse from top to bottom
        result.append(matrix[row][column_end - 1])
    column_end = column_end - 1

    
    if row_start < row_end:# Traverse from right to left
        for column in range(column_end - 1, column_start - 1, -1):
            result.append(matrix[row_end - 1][column])
        row_end = row_end - 1

    
    if column_start < column_end:# Traverse from bottom to top
        for row in range(row_end - 1, row_start - 1, -1):
            result.append(matrix[row][column_start])
        column_start = column_start + 1

for value in result:
    print(value, end=' ')
