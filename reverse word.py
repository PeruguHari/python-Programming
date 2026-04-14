word=input("ENter the string= ")
rev=""
for i in word:
    rev=i+rev
print(rev,end=" ")

"""num=int(input("Enter the number= "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print(rev,end=" ")
    """