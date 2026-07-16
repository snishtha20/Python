import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1)
print(a2)


# scalar operations
# arithmetic

print(a1+5)
print(a1-5)
print(a1*5)
print(a1/5)
print(a1**5)

# relational
print(a1>5)
print(a1<15)
print(a1>=10)
print(a1==15)


# vector operations
# arithmetic
print(a1*a2)
print(a1+a2)
print(a1-a2)
print(a1/a2)

