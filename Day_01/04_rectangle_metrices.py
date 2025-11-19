#Length and breadth of a rectangle and calculate its area and perimeter
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

#Formula for area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

#Displaying the results
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)