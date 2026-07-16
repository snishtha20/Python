# # NumPy array v/s Python List
# Why is NumPy Faster than Python Lists?
# 1. Static Array (NumPy)
# NumPy arrays have a fixed size once created.
# Memory is allocated contiguously (continuous memory locations).
# The CPU can access elements directly without resizing overhead.
# This results in faster indexing, traversal, and computations.

# 2. Dynamic Array (Python List)
# Python lists are dynamic, meaning they can grow or shrink.
# Whenever the list becomes full, Python may allocate a larger block of memory and copy all existing elements to the new location.
# This resizing process increases execution time.


# Referential vs Non-Referential
# Python List – Referential Array
# A Python list does not store the actual values directly. Instead, it stores references (memory addresses/pointers) to Python objects.

# NumPy Array – Non-Referential Array
# A NumPy array stores the actual values directly in contiguous memory (for standard numeric dtypes), rather than storing references for each element.

# speed
# list
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c = []

import time 
start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start)

# numpy
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c= a+b
print(time.time()-start)


# memory
# list
a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

# numpy
# a = np.arange(10000000) #int64 default
# a = np.arange(10000000,dtype=np.int32)
# a = np.arange(10000000,dtype=np.int16)
a = np.arange(10000000,dtype=np.int8)
print(sys.getsizeof(a))


# convenience
# In list, we had to use loop to add items whereas in numpy we added directly