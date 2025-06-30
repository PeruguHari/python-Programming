n=int(input("Enter the total numbers= "))
x=int(input("Enter  x number to divide = "))
y=int(input("Enter y number to divide= "))
for i in range(1,n+1):
    if x!=0 and y!=0:
        if (i%x==0) and (i%y==0):
            print("FizzBuzz")
        elif (i%x==0):
            print("Fizz")
        elif (i%y==0):
            print("Buzz")
        else:
            print(i)
    else:
        print("invalid")
        break