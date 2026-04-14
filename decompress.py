word=input("ENTER THE COMPRESSED WORD= ")
decompress=""
i=0
while i<len(word):
    char=word[i]
    i+=1
    count=""
    while i<len(word) and word[i].isdigit():
        count+=word[i]
        i+=1
    decompress+=char*int(count)
print(decompress)
