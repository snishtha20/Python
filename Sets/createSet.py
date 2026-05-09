# empty
s = set()
print(s)
print(type(s))

# 1D and 2D
s1 = {1,2,3}
print(s1)
#s2 = {1,2,3,{4,5}}
#print(s2)

# homo and hetro
s3 = {1,'hello',4.5,(1,2,3)}
print(s3)

# using type conversion
s4 = set([1,2,3])
print(s4)

# duplicates not allowed
s5 = {1,1,2,2,3,3}
print(s5)

# set can't have mutable items
s6 = {1,2,[3,4]}
print(s6)