num=int(input("Enter the number= "))
squ=num*num
car=len(str(num))
power=10**car
left=squ%power
right=squ//power
if left+right==num:
    print("it is karperkar number")