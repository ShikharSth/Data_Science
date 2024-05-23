# Given two 1-dimensional arrays, perform element-wise addition, subtraction, multiplication, and division.
Arr1 = np.array([1, 2, 3, 4, 5])
Arr2 = np.array([6, 7, 8, 9, 10])
Add = Arr1+Arr2
Add
Sub = Arr1-Arr2
Sub
Mul = Arr1*Arr2
Mul
div = Arr1/Arr2
div

# Calculate the mean, median, and standard deviation of a given 1- dimensional array.
Arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(Arr)
mean
median = np.median(Arr)
median
std = np.std(Arr)
std

# Reshape a 1-dimensional array into a 2-dimensional array of shape (3, 4).
Arr = np.arange(12)
twod_Arr = Arr.reshape((3,4))
twod_Arr
