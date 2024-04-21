import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Print the array
print("Original array:", arr)

# Perform some operations
print("Sum of array elements:", np.sum(arr))
print("Mean of array elements:", np.mean(arr))
print("Maximum element of array:", np.max(arr))
print("Index of maximum element:", np.argmax(arr))


print("\n\nBasic Matrix Program")

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Print the matrices
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Matrix addition
C = A + B
print("\nMatrix addition (A + B):")
print(C)

# Matrix multiplication
D = np.dot(A, B)
print("\nMatrix multiplication (A * B):")
print(D)
