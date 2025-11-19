#Time conversion from minutes to hours and vice versa
# Get user input
time = float(input("Enter time: "))
unit = input("Is this in Minutes or Hours? (M/H): ")    

# Perform conversion based on the unit
#M to H: M / 60
#H to M: H * 60
#upper() method is used to handle both lowercase and uppercase inputs
if unit.upper() == "M":
    print(time / 60, "Hours")
elif unit.upper() == "H":
    print(time * 60, "Minutes")
else:
    print("Invalid unit! Please enter M or H.") 
    