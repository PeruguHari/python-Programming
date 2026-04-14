word=input("Enter the string= ")
long=""
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        sub=word[i:j]
        if sub==sub[::-1]:
            if len(sub)>len(long):
                long=sub
print(long)
print(len(long))