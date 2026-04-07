set = {1,2,3,4}

# print(set)

# set.add(5)
# print(set)

# set.remove(5)
# print(set)

# set.pop() 
# print(set)

# set.clear()
# print(set)


set1 = {3,4,5,6}

print(set.union(set1))

print(set.intersection(set1))


# All Python Set Methods

# Sets are unordered, mutable, and contain unique elements.

# 🔹 1. Adding Elements
# add()
# Adds a single element
# s = {1, 2}
# s.add(3)
# # {1, 2, 3}

# update()
# Adds multiple elements (from iterable)
# s = {1, 2}
# s.update([3, 4])
# # {1, 2, 3, 4}


# 🔹 2. Removing Elements
# remove()
# Removes element (error if not found)
# s = {1, 2, 3}
# s.remove(2)
# # {1, 3}

# discard()
# Removes element (no error if not found)
# s = {1, 2, 3}
# s.discard(5)
# # No error

# pop()
# Removes and returns a random element
# s = {1, 2, 3}
# s.pop()   # random element removed

# clear()
# Removes all elements
# s.clear()
# # set()


# 🔹 3. Set Operations (Very Important 🔥)
# union()
# Combines two sets
# a = {1, 2}
# b = {2, 3}
# a.union(b)   # {1, 2, 3}

# intersection()
# Common elements
# a.intersection(b)   # {2}

# difference()
# Elements in first set but not in second
# a.difference(b)   # {1}

# symmetric_difference()
# Elements in either set but not both
# a.symmetric_difference(b)   # {1, 3}


# 🔹 4. Updating Sets (In-place Operations)
# intersection_update()
# a = {1, 2, 3}
# a.intersection_update({2, 3, 4})
# # {2, 3}

# difference_update()
# a = {1, 2, 3}
# a.difference_update({2})
# # {1, 3}

# symmetric_difference_update()
# a = {1, 2}
# a.symmetric_difference_update({2, 3})
# # {1, 3}


# 🔹 5. Checking Relationships
# issubset()
# {1, 2}.issubset({1, 2, 3})   # True

# issuperset()
# {1, 2, 3}.issuperset({2})   # True

# isdisjoint()
# Returns True if no common elements
# {1, 2}.isdisjoint({3, 4})   # True


# 🔹 6. Copying
# copy()
# s = {1, 2}
# new_s = s.copy()



# 🎯 Important Points (Exam + Interview)
# Sets:
# Do not allow duplicates
# Are unordered
# Are mutable
# Fast for:
# Membership testing (in)
# Removing duplicates

# 💡 Bonus
# Convert list → set (remove duplicates)
# lst = [1, 2, 2, 3]
# set(lst)   # {1, 2, 3}