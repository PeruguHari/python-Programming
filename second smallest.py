num=list(map(int, input("Enter the number= ").split()))
smallest=float('inf')
sec_small=float('inf')
largest=float('-inf')
sec_large=float('inf')
for i in num:
    if i<smallest:
        sec_small=smallest
        smallest=i
    elif smallest<i<sec_small:
        sec_small=i
    if i>largest:
        sec_large=largest
        largest=i
    elif largest>i>sec_large:
        sec_large=i
print(sec_large,sec_small)