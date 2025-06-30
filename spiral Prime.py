n=int(input("ENter the number= "))
matrix=[[0 for _ in range(n)] for _ in range(n)]
top,left,bottom,right=0,0,n-1,n-1
def is_prime(prime):
    if prime<2:
        return False
    for i in range(2,int(prime**0.5)+1):
        if prime%i==0:
            return False
    return True
num=2
while top<=bottom and left<=right:
    for i in range(left,right+1):
        while not  is_prime(num):
            num+=1
        matrix[top][i]=num
        num+=1
    top+=1
    for i in range(top,bottom+1):
        while not  is_prime(num):
            num+=1
        matrix[i][right]=num
        num+=1
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            while not  is_prime(num):
                num+=1
            matrix[bottom][i]=num
            num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            while not  is_prime(num):
                num+=1
            matrix[i][left]=num
            num+=1
        left+=1
for i in matrix:
    print(" ".join(map(str,i)))
