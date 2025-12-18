# Check the capacity of a water bottle


capacity = float(input("Enter the capacity of the water bottle in liters: "))

if capacity < 0.5:
    print("Small Bottle")
elif 0.5 <= capacity <= 1.5:
    print("Medium Bottle")
else:
    print("Large Bottle")   

