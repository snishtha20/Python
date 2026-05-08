# Operations on Lists
# Arithmetic
# Membership
# Loops

# Arithmetic (+ ,*)

L1 = [1,2,3,4]
L2 = [5,6,7,8]

# Concatenation/Merge
print(L1 + L2)

print(L1*3)


L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 in L1)
print(5 not in L1)
print([5,6] in L2)


# Loops
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in L3:
  print(i)

# 2 ways to traverse a list
# itemwise
# indexwise

# itemwise
L = [1,2,3,4]

for i in L:
  print(i)

# indexwise
L = [1,2,3,4]

for i in range(0,len(L)):
  print(L[i])
