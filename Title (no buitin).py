word=input("ENter the string= ")
result=""
start=True
for i in word:
    if start==True:
        if 'a'<=i<='z':
            result+=chr(ord(i)-32)
        else:
            result+=i
        start=False
    else:
        if 'A'<=i<='Z':
            result+=chr(ord(i)+32)
        else:
            result+=i
    if i==" ":
        start=True
print(result,end=" ")

