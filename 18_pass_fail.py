# Determine if a student has passed or failed based on their marks, with grace marks consideration.
marks = int(input("Enter your marks: "))


if marks >= 40:                                # 40 and above: Pass
    print("Result: Pass")                      
elif marks >= 35:                              # 35 to 39: Pass with grace marks
    print("Result: Pass (with grace marks)")
else:                                          # Below 35: Fail
    print("Result: Fail")