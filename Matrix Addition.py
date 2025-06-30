# Matrix size input
rows = int(input("Rows count cheppandi: "))
cols = int(input("Columns count cheppandi: "))

# First matrix input
print("First matrix values enter cheyyandi:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"matrix1[{i}][{j}] = "))
        row.append(value)
    matrix1.append(row)

# Second matrix input
print("Second matrix values enter cheyyandi:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"matrix2[{i}][{j}] = "))
        row.append(value)
    matrix2.append(row)

# Matrix Addition
addition_result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    addition_result.append(row)

# Matrix Subtraction
subtraction_result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    subtraction_result.append(row)

# Results print cheyyadam
print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nAddition Result:")
for row in addition_result:
    print(row)

print("\nSubtraction Result:")
for row in subtraction_result:
    print(row)
