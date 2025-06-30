total=1000
while True:
    print("\n Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    num=int(input("Enter the number= "))
    if num==1:
        print(total)
    elif num==2:
        deposit=int(input("enter the amount"))
        if deposit >0:
            total+=deposit
            print("balance= ",total)
        else:
            print("Invalid ")
    elif num==3:
        withdraw=int(input("Enter the amount= "))
        if withdraw <=total:
            total-=withdraw
            print(total)
        else:
            print("Insufficient ")
    elif num==4:
        print("Thank you")
        break
    else:
        print("Invalid ..! Try again")
        break