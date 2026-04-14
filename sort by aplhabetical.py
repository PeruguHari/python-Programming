word=input("Enter the string= ").split()
for i in range(len(word)):
    for j in range(i+1,len(word)):
        if word[i]>word[j]:
            word[i],word[j]=word[j],word[i]
char=""
for i in word:
    char+=i+" "
print(char)