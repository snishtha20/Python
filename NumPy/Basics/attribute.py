# Array Attributes
import numpy as np
a1 = np.arange(10, dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2) #(how many 2d arrays, rows in 2d array, columns in 2d array)

# print(a1)
# print(a2)
# print(a3)


# # ndim: tells dimensional
# print(a1.ndim)
# print(a2.ndim)
# print(a3.ndim)

# # shape:tells rows,columns
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)

# # size: tells no of items
# print(a1.size)
# print(a2.size)
# print(a3.size)

# itemsize: tells how many memory size occupied by items
# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)

# # dtype: tells data type
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)

# Changing Datatype: It's use is to reduce memory size of that column which don't need excess memory like age column needs int not float
# astype
print(a3.astype(np.int32).dtype)
