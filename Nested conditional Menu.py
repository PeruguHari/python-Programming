print("Menu:\n1. Coffee\n2. Tea")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("1. Espresso: ₹50\n2. Cappuccino: ₹60")
    coffee_type = int(input("Enter type: "))
    if coffee_type == 1:
        print("Price: ₹50")
    elif coffee_type == 2:
        print("Price: ₹60")
    else:
        print("Invalid choice")
elif choice == 2:
    print("1. Green Tea: ₹40\n2. Black Tea: ₹35")
    tea_type = int(input("Enter type: "))
    if tea_type == 1:
        print("Price: ₹40")
    elif tea_type == 2:
        print("Price: ₹35")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
