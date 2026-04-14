num=list(map(int, input("Enter the number= ").split()))
min1=min2=float('inf')
max1=max2=float('-inf')
for i in num:
    if i<min1:
        min2=min1
        min1=i
    elif min1<i<min2:
        min2=i
    if i>max1:
        max2=max1
        max1=i
    elif max1>i>max2:
        max2=i
product1=max1*max2
product2=min1*min2
print(max(product1,product2))