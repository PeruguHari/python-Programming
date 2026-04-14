n=input("Enter the word= ")
long=""
current=""
for i in n:
    if i not in current:
        current=current+i
    else:
        if len(current)>=len(long):
            long=current
        while i in current:
            current=current[1:]
        current=current+i
if len(current)>=len(long):
    long=current
print(long,end=" ")