num=list(map(int, input("Enter the numners= ").split()))
subset=[[]]
for i in num:
    new=[]
    for j in subset:
        new.append(j+[i])
    subset.extend(new)
print(subset,end=" ")