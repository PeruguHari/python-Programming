word=input("Enter the string= ")
result=""
i=0
while i<len(word):
    char=word[i]
    i+=1
    count=""
    while i<len(word) and word[i].isdigit():
        count+=word[i]
        i+=1
    result+=char*int(count)
print(result)

