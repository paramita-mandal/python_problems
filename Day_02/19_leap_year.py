# Determine if a year is a leap year or not
year = int(input("Enter a year: "))

# Leap year if divisible by 4 and not divisible by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")    