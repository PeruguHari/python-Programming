row=int(input("Enter the no.of rows= "))
col=int(input("Enter the no.of cols= "))
matrix=[]
for i in range(row):
    rows=list(map(int, input(f"Enter each {i}row = ").split()))
    matrix.append(rows)
transpose=[]
for i in range(col):
    new=[]
    for j in range(row):
        new.append(matrix[j][i])
    transpose.append(new)
for i in transpose:
    print(*i)