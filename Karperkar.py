import math
num=int(input())
total=0
arr=[]
for _ in range(1,num+1):
    array=int(input())
    arr.append(array)
    total+=array
mean=total/num
s=[(i-mean)**2 for i in arr]
s_num=sum(s)
one=math.sqrt(s_num)
total_mean=one/num
print(total_mean)