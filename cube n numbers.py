num=int(input("Enter the n natural numbers= "))
cube=0
for i in range(1,num+1):
    cube+=i*i*i
    print(cube,end=" ")