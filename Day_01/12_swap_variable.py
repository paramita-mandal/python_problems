#Swap two variables without a third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#Output the original values
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a

#Output the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
 
