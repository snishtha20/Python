def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x) 
# 5
# 6
# 5

def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)
# 2
# 5

def h(y):
    x += 1
x = 5
h(x)
print(x)
# generate error because local variable can't change global's value and cannot access local variable 'x' where it is not associated with a value

def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)
# in f(x): x= 4
# 4
# 3