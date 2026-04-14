n=input("Enter the string= ")
encode=""
for i in n:
    if 'a'<=i<='z':
        encode+=chr((ord(i)-ord('a')+2)%26 + ord('a'))
    elif 'A'<=i<='Z':
        encode+=chr((ord(i)-ord('A')+2)%26 + ord('A'))
    else:
        encode+=i
print(encode)