num=list(map(int, input("ENter the numbers= ").split()))
count=len(num)
recipocal=0
for i in num:
    recipocal+=1/i
harmonic_mean=count/recipocal
print(harmonic_mean,end=" ")
