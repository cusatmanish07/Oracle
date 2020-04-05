import numpy as np

#Print Version of numpy
print(np.__version__)

#Create an array in numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr2 = np.array(["a", "b", "c", "d", "e"])
print(arr2)

arr3 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(arr3)

#Print the dimension of array
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)

#Initialize and print 2D/3D array
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)
print(arr4.ndim)

arr5 = np.array([[[1, 2, 3,], [4, 5, 6]], [[9, 8, 7], [12, 13, 14]]])
print(arr5)
print(arr5.ndim)

# 0D array example 
arr6 = np.array(47)
print(arr6)
print(arr6.ndim)

#1D example 

arr7 = np.array([47])
print(arr7)
print(arr7.ndim)

#Create Nth Dimension of Array 

arr8 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr8)
print("Number of dimension:", arr8.ndim)
