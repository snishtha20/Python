# empty
t1 = ()
print(t1)

# create a tuple with a single item
t2 = ('hello')
print(t2) #hello not ('hello')
print(type(t2)) #str

t2 = ('hello',)
print(t2)
print(type(t2))

# homo
t3 = (1,2,3,4)
print(t3)

# hetro
t4 = (1,2.5,True,[1,2,3])
print(t4)

# tuple
t5 = (1,2,3,(4,5))
print(t5)

# using type conversion
t6 = tuple('hello')
print(t6)


# Accessing Items
# Indexing
# Slicing

print(t3)
print(t3[0])
print(t3[-1])


print(t3[1:3])
print(t5[-1][0] )