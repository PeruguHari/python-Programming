import time
red=int(input("Enter the number= "))
yellow=int(input("Enter the number= "))
green=int(input("Enter the time delay= "))
while True:
    print("red light on wiat until")
    for i in range(red,0,-1):
        print(i,"seconds to go")
        time.sleep(1)
    print("yellow light is on until")
    for i in range(yellow,0,-1):
        print(i,"seconds to go")
        time.sleep(1)
    print("Green is going to completing in ")
    for i in range(green,0,-1):
        print(f"{i} seconds")
        time.sleep(1)
