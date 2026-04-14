num=input("Enter the number= ")
total=0
for i in num:
    total+=int(i)
while total>=10:
    digit=0
    while total>0:
        digit+=total%10
        total//=10
    total=digit
print(total)
