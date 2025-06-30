n=input("Enter the string= ")
res=""
word=""
for i in n:
    if i!=" ":
        word+=i
    else:
        if len(word)>0:
            first=chr(ord(word[0])-32) if 'a'<=word[0]<='z'else word[0]
            rest=""
            for i in word[1:]:
                rest+=chr(ord(i)+32) if 'A'<=i<='Z'else i
            res+=first+rest+" "
            word=""
if len(word)>0:
    first=chr(ord(word[0])-32) if 'a'<=word[0]<= 'z' else word[0]
    rest=""
    for i in word[1:]:
        rest+=chr(ord(i)+32) if 'A'<=i<='Z'else i
    res+=first+rest+" "
print(res)