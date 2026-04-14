import re
email=input("Enter the email= ")
pattern=r'^[a-zA-Z0-9]+@[a-zA-z0-9]+\.[a-zA-z]{2,}$'
if re.findall(pattern,email):
    print("it is valid email")
else:
    print("not Invalid Email")
