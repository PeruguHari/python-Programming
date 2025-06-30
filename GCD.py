num=list(map(int, input("Enter the number= ").split()))
gcd=0
min_num=min(num)
for i in range(1,min_num+1):
    if all(x%i==0 for x in num):
        gcd=i
print(gcd,end=" ")