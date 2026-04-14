num=int(input("Enter the number= "))
for i in range(num):
    for j in range(num):
        if(i+j)%2==0:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
