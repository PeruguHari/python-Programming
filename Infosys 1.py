arr=[5, 8, 7, 6, 10, 22, 9, 5]
n=len(arr)
start=0
dir=1
res=[]
for i in range(n):
    res.append(arr[(start + i*dir)%n])
xor=0
total=0
for i in res:
    xor^=i
    total+=xor
print(total)


