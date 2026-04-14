word=input("Enter the string= ")
result=word[0]
for i in range(1,len(word)):
    if word[i]!=word[i-1]:
        result+=word[i]
print(result,end=" ")