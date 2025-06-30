tot_mem=int(input("enter the total member= "))
tot_bill=int(input("enter the total bill amount"))
if tot_mem>0:
    if tot_bill >0:
        share=tot_bill/tot_mem
        print("did you add tip percentage (yes/no)")
        n=input()
        if n=="yes":
            tip=int(input("enter the tip %= "))
            total=share + (tip/100)*100
            print(total)
        elif n=="no":
            print(share)
        else:
            print("invalid")
    else:
        print("enter the bill amount above 0")
else:
    print("enter the members more than 0")

