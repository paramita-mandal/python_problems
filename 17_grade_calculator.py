# Grade Calculator to determine letter grades based on marks

marks = int(input("Enter your marks: "))

# If-Else Ladder to determine the grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
