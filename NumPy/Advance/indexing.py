# Advance indexing

# Fancy Indexing: it allows to index any row or coulmn if pattern is not forming
import numpy as np
# a= np.arange(24).reshape(6,4)
# print(a)
# print(a[[0,1,3]])
# print(a[:,[0,2,3]])

# Boolean Indexing
b= np.random.randint(1,100,24).reshape(6,4) #randint(start,end,no of parts). It is a way of generating 2d array consists random numbers
print(b)

# find all numbers greater than 50
print(b[b>50])
# find out even numbers
print(b[b%2==0])
# find all numbers greater than 50 and are even
print(b[(b>50) & (b%2==0)])
# find all numbers not divisible by 7
print(b[~(b % 7==0)])