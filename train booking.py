rows=5
cols=4
seats=[["Available" for _ in range(cols)] for _ in range(rows) ]
while True:
    print("\nRailway Seat Booking System:")
    print("1. View Seating Arrangement")
    print("2. Book a Seat")
    print("3. Cancel a Booking")
    print("4. Exit")
    num=int(input("Enter the number= "))
    if num==1:
        for i in range (rows):
            print(f"Rows{i+1}",end=" ")
            for j in range(cols):
                print(f"{seats[i][j]:<10}",end=" ")
            print()
    elif num==2:
        row=int(input("Enter the no.of rows"))
        col=int(input("Enter the no.of cols"))
        if row<0 or row>=rows or col<0 or col>=cols:
            print("Invalid selection")
        elif seats[row][col]=="Booked":
            print("already booked ")
        else:
            name=input("Enter the details")
            seats[row][col]=="available"
            print("Sucessfully Booked")
    elif num==3:
        row=int(input("Enter the number= "))
        col=int(input("Enter the number= "))
        if row<0 or row>=rows or col<0 or col>=cols:
            print("Invalid Selection")
        elif seats[row][col]=="Available":
            print("no seat found to  Delete seating")
        else:
            seats[row][col]=="Available"
            print("succeessfully Deleted")
    elif num==4:
        print("Thanks for visting")
        break
    else:
        print("invalid select required numbers only..!!")





