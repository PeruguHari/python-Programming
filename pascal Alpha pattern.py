n=int(input("Enter the number= "))
num=0
for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(chr(65+num),end=" ")
        num+=1
    print()