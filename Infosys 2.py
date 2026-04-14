n=list(map(int, input("Enter the array= ").split()))
total=0
while len(n)!=0:
    if n[0]!=n[-1]:
        n.pop()
        n.pop(0)
    else:
        n.pop(0)
    total+=1
print(total)
    