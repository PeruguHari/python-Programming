num=list(map(int, input("Enter the nuumber= ").split()))
k=int(input("Enter the number of times= "))
n=len(num)
k=k%n
rotate=[]
for i in range(n,n-k):
    rotate.append(num[i])
for i in range(n-k,n):
    rotate.append(num[i])
print(rotate,end=" ")