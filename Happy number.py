num=int(input("Enter the number= "))
seen=set()
while num!=1 and num not in seen:
    seen.add(num)
    happy=0
    temp=num
    while temp>0:
        digit=temp%10
        happy+=digit*digit
        temp//=10
    num=happy
if num==1:
    print("It is happy number")