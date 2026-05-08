# Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

# print(list(zip(L1,L2)))

L = [i+j for i,j in zip(L1,L2)]
print(L)