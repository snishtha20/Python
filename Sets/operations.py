s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# Union(|)
print(s1 |s2)

# Intersection(&)
print(s1 &s2)

# Difference(-): contains in s1 not in s2
print(s2 -s1)
print(s1 -s2)

# Symmetric Difference(^): show all elements of both sets except common
print(s1 ^s2)

# Membership Test
print(1 in s2)
print(1 not in s2)


# Iteration
for i in s1:
    print(i)