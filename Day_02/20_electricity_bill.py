# Electricity Bill Calculator
# This program calculates the electricity bill based on the number of units consumed.
# The billing rates are as follows:
# Assume slab rates:
#-0–100 units → ₹5 per unit
#-101–200 units → ₹7 per unit
#-Above 200 units → ₹10 per unit

units = int(input("Enter the number of units consumed: "))

#if else statement to calculate bill amount based on slab rates
if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = (100 * 5) + (units - 100) * 7
else:
    bill_amount = (100 * 5) + (100 * 7) + (units - 200) * 10    

print("Total Electricity Bill: ₹", bill_amount)