start=int(input("Enter the start number= "))
end=int(input("Enter the end number= "))
for i in range(start,end):
    sum=0
    for j in range(1,i-1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,end=" ")