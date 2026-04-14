num=int(input("Enter the number= "))
n=num
div=2
while div * div<=n:
    if n%div==0:
        print(div)
        n//=div
    else:
        div+=1
if n>1:
    print(n,end=" ")
