num=list(map(int, input("Enter the number= ").split()))
n=len(num)
for i in range(n):
    index=i
    for j in range(i+1,n):
        if num[j]<num[index]:
            index=j
    num[i],num[index]=num[index],num[i]
print(num,end=" ")
