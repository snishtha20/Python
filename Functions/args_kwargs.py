# *args and **kwargs
# *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function

# *args
# allows us to pass a variable number of non-keyword arguments to a function.

# def multiply(*args):
#     product = 1
#     for i in args:
#         product = product * i
#     print(product)
    

# multiply(1,2,3,4,5,6,7,8,9)


# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->', value)
    
display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')


# Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# The words “args” and “kwargs” are only a convention, you can use any name of your choice

