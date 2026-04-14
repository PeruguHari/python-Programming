start=int(input("Ente the number to start= "))
end=int(input("Enter the number to end= "))
for i in range(start,end+1):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if i==rev:
        print(i,end=" ")