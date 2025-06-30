tot=int(input("enter the total= "))
if tot<1000:
    print("NO Discount")
elif 1000< tot <5000:
    dis=tot*10/100
    print("discount amount =",dis)
    discount=tot-tot*10/100
    print("total price= ",discount)
elif 5000< tot <10000:
    dis=tot*20/100
    print("discount amount =",dis)
    discount=tot-tot*20/100
    print("total price= ",discount)
elif tot >10000:
    dis=tot*30/100
    print("discount amount =",dis)
    discount=tot-tot*30/100
    print("total price= ",discount)
else:
    print("Something you missed ")


