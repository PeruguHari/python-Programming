num=list(map(int, input("ENter the numbers= ").split()))
unique=[]
for i in  num:
    if i not in unique:
        unique.append(i)
print(unique,len(unique))