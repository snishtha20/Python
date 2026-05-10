# Frozenset
# Frozen set is just an immutable version of a Python set object

s = frozenset([1,2,3])
print(s)

# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

fs1 | fs2

# All readbale functions can apply

# what works and what does not
# works -> all read functions
# does't work -> write operations

# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
print(fs)