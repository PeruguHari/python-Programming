n=int(input("Enter the number= "))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()
