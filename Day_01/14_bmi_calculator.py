#Compute BMI (kg/m²)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)
