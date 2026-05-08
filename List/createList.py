null_list = []
print(null_list)
null_list.append("Nishtha")
print(null_list)

# Empty
print([])
# 1D -> Homo
print([1,2,3,4,5])
# 2D
print([1,2,3,[4,5]])
# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])
# Hetrogenous
print([1,True,5.6,5+6j,'Hello'])
# Using Type conversion
print(list('hello'))  #['h', 'e', 'l', 'l', 'o']


# Slicing is same as string
# Accessing Items from a List
# Indexing
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
#positive
print(L[0][0][1])

# Slicing
L = [1,2,3,4,5,6]

print(L[::-1])