# Lambda Function
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


# lambda a,b: a+b

# lambda keyword: creates lambda expression
# a,b : Parameters- One or more parameters are supported. Must be seperated by a comma(,) and no paranthesis
# : Colon- this is a cue for the expression.
# a+b: Expression- must be a single valid python expression

# x -> x^2
b=lambda x: x**2
print(b(10))


# x,y -> x+y
a =lambda x,y: x+y
print(a(5,2))

# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable
# Then why use lambda functions?
# They are used with HOF

# check if a string has 'a'
a=lambda s: 'a' in s
print(a('Nishtha'))

# odd or even
a = lambda x: 'even' if x%2==0 else 'odd'
print(a(72))

# Higher Order Functions(HOF)
def transform(f, L):
    output = []
    for i in L:
        output.append(f(i))

    return output

L=[1,2,3,4,5]

print(transform(lambda x:x**2, L))

# Map
# square the items of a list
print(list(map(lambda a:a**3, [1,2,3,4])))

# odd/even labelling of list items
print(list(map(lambda a: 'even' if a%2==0 else 'odd', [2,3,4,5])))

# fetch names from a list of dict
users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

print(list(map(lambda users: users['name'], users)))


# Filter

# numbers greater than 5
L=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x>5, L)))

# fetch fruits starting with 'a'
fruits = ['apple', 'banana', 'avocado', 'cherry']
print(list(filter(lambda x:x.startswith('a'), fruits)))



# Reduce
# sum of all item
import functools
print(functools.reduce(lambda x,y:x+y, [1,2,3,4,5]))

# find min
import functools
print(functools.reduce(lambda x,y: x if x<y else y, [5,3,6,1,7,8]))

