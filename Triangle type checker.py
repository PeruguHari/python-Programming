A=int(input("Enter the Number= "))
B=int(input("Enter the Number= "))
C=int(input("Enter the Number= "))
if(A+B>C and B+C>A and C+A>B):
    print("t is Valid Triangle and")
    if(A==B==C):
        print("It is Equilateral Triangle")
    elif(A==B or B==C or C==A):
        print("It is Isosceles Triangle")
    elif(A!=B or B!=C or C!=A):
        print("It is Scalene Triangle")
else:
    print("it is invalid triangle")