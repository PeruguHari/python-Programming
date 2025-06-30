height=float(input("enter the height= "))
weight=float(input("enter the weight= "))
BMI=weight/(height**2)
if BMI< 18.5:
    print("underweight")
elif 18.5 < BMI<25:
    print("Normal Weight")
elif 25<BMI<30:
    print("Overweight")
elif 30< BMI>=30:
    print("Obese")
else:
    print("Invlaid")