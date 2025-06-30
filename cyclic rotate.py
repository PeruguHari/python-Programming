num=list(map(int,input("Enter the number= ").split()))
rotations=int(input("Enter the number=  "))
for _ in range(rotations):
    last=num.pop()
    num.insert(0,last)
print(num)