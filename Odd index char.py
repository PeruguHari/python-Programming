num=input("Enter the numbers= ").split()
odd=[]
for i in range(len(num)):
    if i%2!=0:
        odd+=num[i]
print(odd,end=" ")
        