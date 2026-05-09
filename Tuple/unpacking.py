# Special Syntax
# tuple unpacking
# a,b,c = (1,2,3)
# print(a,b,c)


# a,b = (1,2,3)
# print(a,b)

# Swap
a = 1
b = 2
a,b = b,a

print(a,b)


# if u want to use only starting 2 variables
a,b,*others = (1,2,3,4)
print(a,b)
print(others)