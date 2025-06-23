rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix_2d = []
print("Enter the elements row by row:")

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element at row {i+1}, column {j+1}: "))
        row.append(val)
    matrix_2d.append(row)
print("original matrix :")
for row in matrix_2d:
    print(row)

rotated_matrix = []
for i in range(cols):
    row = []
    for j in range(rows - 1, -1, -1):
        row.append(matrix_2d[j][i])
    rotated_matrix.append(row)


print("\nRotated Matrix (90 degrees clockwise):")
for row in rotated_matrix:
    print(row) 
