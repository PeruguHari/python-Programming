start=int(input("Enter the start prime number= "))
end=int(input("Enter the end prime number= "))
for i in range(start,end+1):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")

