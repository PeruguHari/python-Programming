n=input("Enter the number= ")
f={}
for i in n:
    if i.isalpha():
        if i in f:
            f[i]+=1
        else:
            f[i]=1
for i,count in f.items():
    print(i,count)