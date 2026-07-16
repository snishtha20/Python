# Broadcasting
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
# The smaller array is “broadcast” across the larger array so that they have compatible shapes.

# same shape
import numpy as np
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
print(a)
print(b)
print(a+b)

# diff shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print(a)
print(b)
print(a+b)

# Broadcasting Rules
# 1. Make the two arrays have the same number of dimensions.
# ~~If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.

# 2. Make each dimension of the two arrays the same size.
# ~~If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# ~~If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.


# More examples

a = np.arange(12).reshape(4,3)
b = np.arange(3)
print(a)
print(b)
print(a+b)

a = np.arange(12).reshape(3,4)
b = np.arange(3)
print(a)
print(b)
print(a+b)

a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)
print(a)
print(b)
print(a+b)

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)
print(a)
print(b)
print(a + b)

a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)
print(a)
print(b)
print(a+b)

a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
print(a)
print(b)
print(a+b)

a = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2,2)
print(a)
print(b)
print(a+b)

