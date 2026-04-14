"""" num=int(input("Enter the number= "))
length=len(str(num))
orginal=num
total=0
while num>0:
    digit=num%10
    total+=digit**length
    num//=10
if total==orginal:
    print("it is arm strong number") """

start=int(input("Enter the starting number= "))
end=int(input("Enter the ending number= "))
for i in range(start,end+1):
    length=len(str(i))
    total=sum(int(j)**length for j in str(i))
    if total==i:
        print(i,end=" ")