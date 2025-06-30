Marks=int(input("Enter the Marks of Student= "))
if(Marks>0):
    if(Marks>=90):
        print("Grade A")
    elif(80<=Marks<90):
        print("Grade B")
    elif(70<= Marks <80):
        print("Grade C")
    elif(60<= Marks <70):
        print("Grade D")
    else:
        print("Grade F")
else:
    print("It is Invalid Number")