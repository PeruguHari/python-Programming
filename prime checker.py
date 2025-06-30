n=int(input("Enter the number= "))
m=int(input("ENter the number= "))
count=0
mth=0
nth=0
n_digit=0
m_digit=0
for i in range(2,10**6):
    prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        count+=1
        if count==n:
            nth=i
        if count==m:
            mth=i
            break
c=(nth*mth)-1
temp=nth
while temp>0 or n_digit >=10:
        if temp==0:
            temp=n_digit
            n_digit=0
        rem=temp%10
        n_digit+=rem
        temp//=10
temp=mth
while temp>0:
     rem=temp%10
     m_digit+=rem
     temp//=10
result=(nth*n_digit)
print(result)
print(c)
