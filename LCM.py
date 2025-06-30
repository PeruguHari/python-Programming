num=list(map(int, input("Enter the number= ").split()))
lcm=1
for i in num:
    great=max(lcm,i)
    while True:
        if great%lcm==0 and great%i==0:
            lcm=great
            break
        great+=1
print(lcm,end=" ")