num=input("Enter the hexa numver= ").upper()
hexa='0123456789ABCDEF'
power=0
decimal=0
for i in num[::-1]:
    value=hexa.index(i)
    decimal+=value*(16**power)
    power+=1
print(decimal,end=" ")