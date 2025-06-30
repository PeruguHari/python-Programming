vehical=input("Enter the vehical type= ")
if (vehical=="car"):
    print(f"Tax for {vehical} is 100$")
elif(vehical=="Truck"):
    print(f"Tax for {vehical} is 200$")
elif(vehical=="Bike"):
    print(f"Tax for {vehical} is 50$")
elif(vehical=="Others"):
    print(f"Tax for {vehical} is 150$")
else:
    print("Invalid Vehical Type")