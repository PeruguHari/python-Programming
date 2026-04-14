n=input("Enter the string1= ").replace(" ","").lower()
m=input("Enter the string2= ").replace(" ","").lower()
freq1={}
freq2={}

if len(n)!=len(m):
    anagram=False
else:
    for i in n:
        freq1[i]=freq1.get(i,0)+1
    for i in m:
        freq2[i]=freq2.get(i,0)+1
    anagram=(freq1==freq2)
print(anagram)