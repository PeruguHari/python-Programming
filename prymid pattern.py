n=int(input("Enter the number= "))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    elif i==n:
        print("* "*(2*n-i))
    else:
        print("*"+" "*(2*i-3)+"*")