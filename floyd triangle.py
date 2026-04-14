num=int(input("ENter the no.of rows= "))
number=1
for i in range(num+1):
    for j in range(i):
        print(number,end=" ")
        number+=1
    print()