def transpose(matrix):
    # Get dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create transposed matrix
    transposed = []
    for j in range(cols):  # For each column in original
        new_row = []
        for i in range(rows):  # For each row in original
            new_row.append(matrix[i][j])  # Take element at (i,j)
        transposed.append(new_row)
    
    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result1 = transpose(matrix)
print("Matrix 1 transposed:")
for row in result1:
    print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result2 = transpose(matrix)
print("\nMatrix 2 transposed:")
for row in result2:
    print(row)