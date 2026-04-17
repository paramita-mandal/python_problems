# Rotate list by K positions

# Step 1: Take input
numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter K: "))

# Step 2: Adjust K
k = k % len(numbers)

# Step 3: Rotate the list
rotated = numbers[-k:] + numbers[:-k]

# Step 4: Print result
print("Rotated list:", rotated)