num=list(map(int, input().split()))
cyclic=int(input())
for _ in range(cyclic):
    last=num.pop()
    num.insert(0,last)
print(num,end=" ")