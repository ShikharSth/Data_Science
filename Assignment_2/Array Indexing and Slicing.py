# Extract the first row and last column of a 2-dimensional array.
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
first_row = arr[0, :]
last_column = arr[:, -1]
first_row
last_column 

# Reverse the order of elements in a 1-dimensional array.
Arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rev = Arr[::-1]
rev

# Select elements from a 2-dimensional array that satisfy a specific condition (e.g., values greater than a certain threshold).
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
greater = arr[arr > 5]
greater
