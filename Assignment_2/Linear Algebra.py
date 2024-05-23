# Calculate the dot product of two 1-dimensional arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
dot = np.dot(arr1, arr2)
dot

# Compute the matrix multiplication of two 2-dimensional arrays.
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
matrix = np.matmul(arr1, arr2)
matrix

# Find the inverse and determinant of a square matrix.
matrix = np.array([[1, 2],
                   [3, 4]])
deter = np.linalg.det(matrix)
deter
