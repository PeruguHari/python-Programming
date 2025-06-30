n=int(input("Enter the units Consumed= "))
if n<=100:
    bill=n*5
    print(bill)
elif n<=200:
    bill=100*5+(n-100)*7
    print(bill)
else:
    bill=100*5 + 200*7+(n-300)*10
    bill=max(5000)
    print(bill)
