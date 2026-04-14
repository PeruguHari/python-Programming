num=eval(input("Enter the nested list= "))
stack=num[::-1]
flat=[]
while stack:
    item=stack.pop()
    if isinstance(item,list):
        stack.extend(item[::-1])
    else:
        flat.append(item)
print(flat)

