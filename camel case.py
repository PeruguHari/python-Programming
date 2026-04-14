n=input("Enter the number= ").split()
camel=n[0].lower()
for i in n[1:]:
    camel=camel+i.capitalize()
print(camel)
