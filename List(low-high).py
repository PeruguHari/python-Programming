num=list(map(int, input("Enter the number= ").split()))
low=num[0]
high=num[0]
for i in num:
    if i>=high:
        high=i
    if i<=low:
        low=i
print("lowest= ",low)
print("highest= ",high)