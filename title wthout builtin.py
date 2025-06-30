num=input("Enter the number= ")
result=" "
for i in range(len(num)):
    if i==0 or num[i-1]==" ":
        if 'a'<=num[i]<='z':
            result+=chr(ord(num[i])-32)
        else:
            result+ num[i]
    else:
        result+= num[i]
print(result,end=" ")