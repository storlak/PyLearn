import numpy as np

# $ | & ^ ~ these are bitwise operators

# Create an array of integers
arr = np.array([5, 12, 7, 18, 3, 10, 14])
# Create a mask that is True for elements greater than 10
mask = arr > 10
# Use the mask to filter elements
filtered_arr = arr[mask]

print("Original array:", arr)
print("Mask:", mask)
print("Filtered array:", filtered_arr)
