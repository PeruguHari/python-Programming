n=int(input("Enter the year= "))
if(n>0):
    if(n%4==0):
        print("It is leap year")
    elif(n%400==0 and n%100!=0):
        print(f"{n} It is leap Year")
    else:
        print(f"{n} It is not leap year")
else:
    print(f"{n} it is less than 0 ..Invalid")