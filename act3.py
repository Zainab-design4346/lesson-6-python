print("BMI calculator")
print("______________")
h=float(input("Enter your height in m: "))
w=float(input("Enter your weight in kg: "))
bmi=w/(h**2)

print("Your BMI is", bmi)

if bmi<18.5:
    print("You are underweight")

elif bmi>18.5 and bmi<25:
    print("You are normal")

elif bmi>25 and bmi<30:
    print("You are overweight")

elif bmi>30:
    print("You are obese")
