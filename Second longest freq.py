word=input("Enter the string= ").split()
freq={}
for i in word:
    freq[i]=freq.get(i,0)+1
long=""
sec_long=""
count=0
sec_count=0
for i in freq:
    if freq[i]>count:
        sec_count=count
        sec_long=long
        long=i
        count=freq[i]
    elif freq[i]>sec_count and freq[i]!=count:
        sec_count=freq[i]
        sec_long=i
print(sec_long,sec_count)
    
