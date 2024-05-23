# Add a scalar value to each element of a 2-dimensional array.
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
scalar = arr + 5
scalar

# Multiply a 1-dimensional array with a 2-dimensional array, leveraging NumPy's broadcasting rules.
array1 = np.array([1, 2, 3, 4])
array2 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])
mul = array1 * array2
mul
