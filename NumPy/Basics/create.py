# Creating Numpy Arrays
import numpy as np
# print(np.array([1,2,3])) #Vectors


# # 2D and 3D
# b = np.array([[1,2,3],[4,5,6]]) #Matrices
# print(b)

# c = np.array([[[1,2],[2,3]], [[1,2],[2,3]]]) #Tensors
# print(c)

# dtype
# print(np.array([1,2,3], dtype=float))
# print(np.array([1,2,3], dtype=bool)) #all non zero values considered as true
# print(np.array([1,2,3], dtype=complex))

# np.arange: similar to range function
# print(np.arange(1,11))
# print(np.arange(1,11,2))

# with reshape: it is a way to put array in tabular like structure
# print(np.arange(10).reshape(2,5)) #(rows, columns)
# print(np.arange(10).reshape(5,2))
# print(np.arange(10).reshape(3,5)) #throw error because rows x columns should be equal to array size.
# print(np.arange(16).reshape(2,2,2,2)) #print 4d array
 

# np.ones and np.zeros: it's input is a tuple 
# These functions are useful when you need to initialize arrays before performing computations. the data type of the array by default, it is float
# print(np.ones((3,4)))
# print(np.zeros((3,4)))
# print(np.zeros((2, 2), dtype=int))

# np.random: will generate random numbers between 0 & 1
# print(np.random.random((3,4))) #random is class then random is method


# # np.linspace: Linear space. It generate equally spaced numbers between interval 
# print(np.linspace(-10,10,10)) #(lower range, upper range, no of parts)

# # np.identity
# print(np.identity(3)) #print 3x3 identity matrix
