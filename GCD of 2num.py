num1=int(input("Enter the 1st number= "))
num2=int(input("Enter the 2nd number= "))
low=min(num1,num2)
gcd=0
for i in range(1,low+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd,end=" ")
