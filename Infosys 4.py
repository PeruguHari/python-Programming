n=int(input("Enter the number of monsters= "))
exp=int(input("Enter your experience level= "))
p=[int(input("Enter the each monsters level= "))for _ in range(n)]
b=[int(input("Enter the each monster bonus= "))for _ in range(n)]
total=0
ans=sorted(zip(p,b))
for power,bonus in ans:
    if power>exp:
        break
    exp+=bonus
    total+=1
print(total)