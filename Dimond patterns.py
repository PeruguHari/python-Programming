n=int(input("Enter the number= " ))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+("*"))
