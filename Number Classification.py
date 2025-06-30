N=int(input("Enter the NUmber= "))
if(N>0):
    if(N%2==0):
        print("It is Positive Even Number")
    else:
        print("It is postive odd number")
elif(N<0):
    if(N%2==0):
        print("It is Negitive Even Number")
    else:
        print("It is Negitive odd number")
else:
    print("It is Zero")
