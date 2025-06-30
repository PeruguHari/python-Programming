n=1
m=1000
count=0
summ=0
for i in range(n,m+1):
    s=len(str(i))
    length=sum(int(digit)**s for digit in str(i))
    if length==i:
        count+=1
        summ+=i
        print(length,end=" ")
print()
print(count)
print(summ)
