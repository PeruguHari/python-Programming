rows=int(input("Enter the number= "))
cols=int(input("Enter the number= "))
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
transpose=[]
for i in range(cols):
    row=[]
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
for row in transpose:
    print(" ".join(map(str,row)))
