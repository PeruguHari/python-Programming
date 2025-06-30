password=input("Enter the Password= ")
if len(password) < 6 :
    print("It is weak")
elif password.isalpha():
    print("it is weak")
elif len(password)>= 6 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and any(not c.isnumeric() for c in password):
    print("it is strong")
else:
    print("it is medium")