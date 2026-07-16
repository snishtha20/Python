# Other Functions

### Iterarting
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

for i in a1:
    print(i)

for i in a2: #print rows
    print(i)

for i in a3: #print 2d arrays
    print(i)

for i in np.nditer(a3): #Returns an iterator that allows efficient element-by-element traversal of a NumPy array.
    print(i)





### Reshaping
# reshape: Done

# Transpose
print(np.transpose(a2))
print(a2.T)

# ravel: Converts a multidimensional NumPy array into a 1D array
print(a3.ravel())





### Stacking
# horizontal stacking
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)
print(a4)
print(a5)
print(np.hstack((a4,a5)))

# Vertical stacking
print(np.vstack((a4,a5)))






### Splitting
# horizontal splitting
print(np.hsplit(a4,4)) #(array, no of equal parts)
# print(np.hsplit(a4,5)) #will throw error 

# vertical splitting
print(np.vsplit(a5,3))