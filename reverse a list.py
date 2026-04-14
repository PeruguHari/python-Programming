"""n=list(map(int, input("Enter the number= ").split()))
left=0
right=len(n)-1
while left < right:
    n[left],n[right]=n[right],n[left]
    left+=1
    right-=1
print(n,end=" ")
"""
num=list(map(int, input("Enter the number= ").split()))
n=[]
for i in range(len(num)-1,-1,-1):
    n.append(num[i])
print(n,end=" ")