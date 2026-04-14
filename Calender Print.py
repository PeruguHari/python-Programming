total=int(input("How manys days you to print= "))
start=int(input("Starting which date you want to print= "))
current=0
print("Sun Mon Tue Wed Thu Fri Sat")
for _ in range(1,start):
    print("  ",end=" ")
    current=start
for i in range(1,total+1):
    print(f"{i} ",end=" ")
    current+=1
    if current>6:
        print()
        current=0
