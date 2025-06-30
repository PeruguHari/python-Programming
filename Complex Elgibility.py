age=int(input("Enter the age= "))
if age>=18:
    n=int(input("Enter how many practice run completed= "))
    if n>=2:
        print("you are eligible to particpate marathon")
    else:
        print("you have to complete atleast 2 practice runs to elgible")
elif age <18 and age >=16:
    print("They need a signed consent form to be eligible")
else:
    print("Not eligible")