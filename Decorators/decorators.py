# Decorators
# A decorator in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it.
# This can happen only because python functions are 1st class citizens.
# A decorator is just a function that takes another function, wraps extra behavior around it, and returns a new function.

# There are 2 types of decorators available in python
# Built in decorators like @staticmethod, @classmethod, @abstractmethod and @property etc
# User defined decorators that we programmers can create according to our needs


# In Python, first-class citizens are entities that are treated like any other object in the language. This means they can be:
# Assigned to variables.
# Passed as arguments to other functions.
# Returned from functions.
# Stored in data structures such as lists, tuples, and dictionaries.
# Created at runtime.

# Python are 1st class function
# def modify(func, num):
#     return func(num)

# def square(num):
#     print(num**num)
# modify(square, 2)


# simple example
# def my_decorator(func):
#     def wrapper():
#         print("************************")
#         func()
#         print("************************")
#     return wrapper

# def hello():
#     print('Hello')


# def display():
#     print('Hello Nishtha')

# a = my_decorator(hello) # we stored it to a variable because we used return statement whenever we use return statement we have to store it.
# a()

# b = my_decorator(display)
# b()

# return wrapper means give back the function itself, without running it yet. Here, wrapper has no (), so it is not executed. The function object is returned. Now 'a' refers to the same function as wrapper.
# So you can call it later. return wrapper
# means “return the wrapper function so someone can call it later.”
# All of these means inner function can access outer function's variables and things even when outer function has closed




# decorator with an argument.
# It checks whether the value passed to function has the correct data type.
# below code is for 1 argument
# def sanity_check(data_type):
#     def outer_wrapper(func):
#         def inner_wrapper(*args):
#             if type(*args) == data_type:
#                 func(*args)
#             else:
#                 print('Invalid data type')

#         return inner_wrapper
#     return outer_wrapper

# @sanity_check(int)
# def square(num):
#     print(num**2)

# square(2)


# below code is for multiple arguments
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if all(type(arg) == data_type for arg in args):
                func(*args)
            else:
                print('Invalid data type')

        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def power(a, b):
    print(a*b)


power(2,3)