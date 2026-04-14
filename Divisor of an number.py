num=int(input("Enter the number= "))
divisor=0
for i in range(1,num+1):
    if num%i==0:
        divisor=i
        print(divisor,end=" ")