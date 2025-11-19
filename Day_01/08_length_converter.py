#Kilometer to meter converter and vice versa
# Get user input
distance = float(input("Enter distance: "))
unit = input("Is this in Kilometers or Meters? (K/M): ")

# Perform conversion based on the unit
#K to M: K * 1000
#M to K: M / 1000
#upper() method is used to handle both lowercase and uppercase inputs
if unit.upper() == "K":
    print(distance * 1000, "Meters")
elif unit.upper() == "M":
    print(distance / 1000, "Kilometers")
else:
    print("Invalid unit! Please enter K or M.") 
