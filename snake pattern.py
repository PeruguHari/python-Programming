n=int(input("Enter the number= "))
num=1
for i in range(n):
    row=[]
    for j in range(n):
        row.append(num)
        num+=1
    if i%2==1:
        row.reverse()
    for k in row:
        print(k,end=" ")
    print()