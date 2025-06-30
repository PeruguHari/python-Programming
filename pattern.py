rows=5
for i in range(rows):
    for j in range(i,rows):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,rows):
        print("*",end=" ")
    print()
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i+1,rows):
        print(" ",end=" ")
    for j in range(i+1,rows):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()