def balanced(lst):
    stack=[]
    parenthess={']':'[','}':'{',')':'('}
    for i in lst:
        if i in '[{(':
            stack.append(i)
        elif i in ']})':
            if  not stack or stack[-1]!=parenthess[i]:
                return False
            stack.pop()
    return len(stack)==0
n=input("ENter the brackets= ")
print(balanced(n))
if balanced(n):
    print("it is balanced")
else:
    print("it is not balanced")
            
