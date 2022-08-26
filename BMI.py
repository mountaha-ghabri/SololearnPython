#This program is an easier way to calculate BMI and find out someone's category by inserting weight in (Kg) and height in (m).
weight=float(input())
height=float(input())
BMI=weight/(height**2)
if BMI<18.5:
    print("Underweight")
elif BMI<25:
    print('Normal')
elif BMI<30:
    print("Overweight")
else:
    print("Obesity")
