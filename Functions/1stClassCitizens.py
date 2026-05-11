# type and id
def square(num):
  return num**2

type(square)

id(square)

# reassign
x = square
id(x)
x(3)

a = 2
b = a
b


# deleting a function
del square
square(3)


# storing
L = [1,2,3,4,square]
L[-1](3)

s = {square}
s

# returning a function
def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))


