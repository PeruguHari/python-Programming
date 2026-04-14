num1=int(input("Enter the 1st number= "))
num2=int(input("Enter the 2nd number= "))
LCM=0
high=max(num1,num2)
while True:
    if high%num1==0 and high%num2==0:
        LCM=high
        break
    high+=1
print(LCM,end=" ")
