num=int(input("Enter the number= "))
binary=""
while num>0:
    n=num%2
    binary=str(n)+binary
    num//=2
print(binary)