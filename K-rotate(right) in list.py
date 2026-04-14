num=list(map(int,input("Enter ht enumber= ").split()))
k=int(input("Enter how many no.to rotate= "))
n=len(num)
k=k%n
rotate=[]
for i in range(k,n):
    rotate.append(num[i])
for i in range(0,k):
    rotate.append(num[i])
print(rotate,end=" ")
