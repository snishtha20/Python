# Indexing
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# print(a1)
# print(a2)
# print(a3)

# print(a1[5])
# print(a2[1,0])
# print(a3[1,0,1])
# print(a3[1,1,0])

# Slicing
print(a1[2:5:2])
print(a2[0:2,1::2])
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0,:])
print(a2[:,2])
print(a2[1:,1:3])
a3 = np.arange(27).reshape(3,3,3)
print(a3)
print(a3[::2,0,::2])
print(a3[2,1:,1:])
print(a3[0,1,:])

