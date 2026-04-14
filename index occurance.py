num=list(map(int, input("Enter the numbers= ").split()))
n=int(input("Enter the index number= "))
result=[]
for i in range(n+1):
    result.append(num[i])
print(result,end=" ")