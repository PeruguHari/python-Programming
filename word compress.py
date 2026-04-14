word=input("Enter the word= ")
res=""
count=1
for i in range(1,len(word)):
    if word[i]==word[i-1]:
        count+=1
    else:
        res+=word[i-1]+str(count)
        count=1
res+=word[-1]+str(count)
print(res)