current=1
while True:
    n=int(input("Enter the required floor= "))
    if n==-1:
        break
    if n==current:
        print("WE are in same floor")
        continue
    if n< current:
        for i in range(current,n-1,-1):
            print(f"{i}")
        print(f"reached= {i}floor")
        current=n
    else:
        if n>current:
            for i in range(current,n+1):
                print(f"{i}")
            print(f"reached= {i}floor")
            current=n
        