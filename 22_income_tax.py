# Income tax calculation 
#Assume Tax Slabs:
# Income ≤ ₹2,50,000 → No tax
# ₹2,50,001 – ₹5,00,000 → 5% tax
# ₹5,00,001 – ₹10,00,000 → 20% tax
# Above ₹10,00,000 → 30% tax

income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 1000000:
    tax = 0.05 * 250000 + 0.20 * (income - 500000)
else:
    tax = 0.05 * 250000 + 0.20 * 500000 + 0.30 * (income - 1000000) 
    
print(f"Your income tax is: ₹{tax}")   #{} is used for variable substitution in f-strings