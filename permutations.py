word=input("Enter the string= ")
permutation=[""]
for i in word:
    new=[]
    for j in permutation:
        for k in range(len(j)+1):
            new.append(j[:k]+i+j[k:])
        permutation=new
print(permutation)