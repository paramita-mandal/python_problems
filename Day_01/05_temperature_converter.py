# Converting temperature between Celsius and Fahrenheit

temp = float(input("Enter temperature: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

# Perform conversion based on the unit
#C to F: (C * 9/5) + 32
#F to C: (F - 32) * 5/9
#upper() method is used to handle both lowercase and uppercase inputs
if unit.upper() == "C":
    print((temp * 9/5) + 32, "F")
elif unit.upper() == "F":
    print((temp - 32) * 5/9, "C")
else:
    print("Invalid unit! Please enter C or F.")
