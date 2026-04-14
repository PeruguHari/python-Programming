def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def spiral(n):
    size=n*n
    prime=[]
    num=2
    while len(prime)<size:
        if is_prime(num):
            prime.append(num)
        num+=1
    matrix=[[0]*n for _ in range(n)]
    top,bottom,left,right=0,n-1,0,n-1
    idx=0
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            matrix[top][i]=prime[idx]
            idx+=1
        top+=1
        for i in range(top,bottom+1):
            matrix[i][right]=prime[idx]
            idx+=1
        right-=1
        for i in range(right,left-1,-1):
            matrix[bottom][i]=prime[idx]
            idx+=1
        bottom-=1
        for i in range(bottom,top-1,-1):
            matrix[i][left]=prime[idx]
            idx+=1
        left+=1
    return matrix
n=int(input("Enter the n*n size= "))
result=spiral(n)
for i in result:
    print(*i)
