import random
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
special='!@#$&'
combine=lower+upper+number+special
n=int(input("Enter the length= "))
password=""
for _ in range(1,n+1):
    password+=random.choice(combine)
print(password,end=" ")
