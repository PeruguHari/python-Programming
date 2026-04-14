word=input("Enter the string= ")
substr=[]
repeated=[]
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        sub=word[i:j]
        substr.append(sub)
for i in substr:
    count=0
    for j in range(len(word)-len(i)+1):
        if word[j:j+len(i)]==i:
            count+=1
    if count>1 and i not in repeated:
        repeated.append(i)
print(repeated,end=" ")