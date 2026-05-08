# len/min/max/sorted
L = [2,1,5,7,0]

print(len(L))
print(min(L))
print(max(L))
print(sorted(L,reverse=True))

# count 
L = [1,2,1,3,4,1,5]
L.count(5)

# index
L = [1,2,1,3,4,1,5]
L.index(1)

# reverse
L = [2,1,5,7,0]
# permanently reverses the list
L.reverse()
print(L)

# sort (vs sorted)
L = [2,1,5,7,0]
print(L)
print(sorted(L)) #create new list
print(L)
L.sort() #modifies original
print(L)

# copy -> shallow means create new
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))