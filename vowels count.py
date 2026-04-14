n=input("Enter the word= ")
vowels='AEIOUaeiou'
vow=0
con=0
for i in n:
    if i in vowels:
        vow+=1
    else:
        con+=1
print("vowels=", vow)
print("consonants= ",con,end=" ")

