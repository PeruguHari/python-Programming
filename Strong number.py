num=int(input("Enter the number= "))
total=0
for i in str(num):
    strong=1
    for j in range(1,int(i)+1):
        strong*=j
    total+=strong
    if total==num:
        print("it is strong number ")