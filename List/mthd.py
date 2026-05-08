list = [2,1,3]

list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(4, 5) #insert(index, element)
print(list)

# Functions
# Lists are mutable (can be changed).
# Most methods modify the list in-place.

# 1. Adding Elements
# a) append()
# Adds an element at the end of the list
# lst = [1, 2, 3]
# lst.append(4)
# # [1, 2, 3, 4]

# b) extend()
# Adds elements from another iterable
# lst = [1, 2]
# lst.extend([3, 4])
# # [1, 2, 3, 4]

# c) insert(index, element)
# Inserts element at a specific position
# lst = [1, 2, 4]
# lst.insert(2, 3)
# # [1, 2, 3, 4]


# 2. Removing Elements
# a) remove()
# Removes first occurrence of value
# lst = [1, 2, 3, 2]
# lst.remove(2)
# # [1, 3, 2]

# b) pop([index])
# Removes and returns element at index (last by default)
# lst = [1, 2, 3]
# lst.pop()
# # returns 3 → [1, 2]

# c) clear()
# Removes all elements
# lst = [1, 2, 3]
# lst.clear()
# # []


# 3. Searching & Counting
# a) index()
# Returns index of first occurrence
# lst = [10, 20, 30]
# lst.index(20)
# # 1

# b) count()
# Counts occurrences of a value
# lst = [1, 2, 2, 3]
# lst.count(2)
# # 2


# 4. Sorting & Reversing
# a) sort()
# Sorts list in ascending order (in-place)
# lst = [3, 1, 2]
# lst.sort()
# # [1, 2, 3]

# Descending:
# lst.sort(reverse=True)

# b) reverse()
# Reverses the list
# lst = [1, 2, 3]
# lst.reverse()
# # [3, 2, 1]


# 5. Copying
# a) copy()
# Returns a shallow copy
# lst = [1, 2, 3]
# new_lst = lst.copy()

# 6.
# len(lst)     # length
# max(lst)     # maximum value
# min(lst)     # minimum value
# sum(lst)     # sum of elements 