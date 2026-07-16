# Array Functions

import numpy as np
a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# max/min/sum/prod
# 0 -> col and 1 -> row 
print(np.max(a1))
print(np.min(a1))
print(np.sum(a1, axis=0))
print(np.prod(a1, axis=1))

# mean/median/std/var
print(np.mean(a1, axis=1))

# trigonomoetric functions
np.sin(a1)

# dot product: for dot product, no. of columns of 1st matrix == no of rows of 2nd matrix
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
print(np.dot(a2, a3))


# log and exponents
print(np.log(a1))
print(np.exp(a1))


# round/floor/ceil
print(np.round(np.random.random((2,3)))*100) #round off
print(np.floor(np.random.random((2,3)))*100) #6.7 -> 6
print(np.ceil(np.random.random((2,3)))*100) #6.7 -> 7

