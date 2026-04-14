word=input("Enter the string= ")
freq={}
for i in word:
    freq[i]=freq.get(i,0)+1
count=0
char=""
for i in freq:
    if freq[i]>count:
        count=freq[i]
        char=i
print(char)
print(count)
