def credit_card(num):
    num=num.replace(" ","")
    if not num.isdigit():
        return False
    total=0
    reverse=num[::-1]
    for i in range(len(reverse)):
        digit=int(reverse[i])
        if i%2==1:
            digit *=2
            if digit>9:
                digit-=9
        total+=digit
    return total %10==0
num=input("Enter the numbers= ")
print("Vlalid credit card number"if credit_card(num)else " Invalid card number")