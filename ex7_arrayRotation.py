matrix_2d = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
rotated_matrix = []

for i in range(len(matrix_2d)):
    row = []
    for j in range(len(matrix_2d) - 1, -1, -1):
        row.append(matrix_2d[j][i])
    rotated_matrix.append(row)
    
for row in rotated_matrix:
    print(row)
    
