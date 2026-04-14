n=int(input("Enter the number to sum= "))
total=0
for i in range(1,n+1):
    total+=1/i
print(f'{total:.5f}',end=" ")