# There are 2 stages where error may happen in a program

# During compilation -> Syntax Error
# During execution -> Exceptions

# Syntax Error
# Something in the program is not written according to the program grammar.
# Error is raised by the interpreter/compiler
# You can solve it by rectifying the program

# Examples of syntax error
print 'hello world'

# Other examples of syntax error
# Leaving symbols like colon,brackets
a = 5
if a==3
  print('hello')

# Misspelling a keyword
a = 5
iff a==3:
  print('hello')

# Incorrect indentation
a = 5
if a==3:
print('hello')

# empty if/else/loops/class/functions


# IndexError
# The IndexError is thrown when trying to access an item at an invalid index.
L = [1,2,3]
print(L[100])


# ModuleNotFoundError
# The ModuleNotFoundError is thrown when a module could not be found.
import mathi
print(math.floor(5.3))


# KeyError
# The KeyError is thrown when a key is not found

d = {'name':'nitish'}
print(d['age'])



# TypeError
# The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
print(1 + 'a') #when we put operations on wrong data type


# ValueError
# The ValueError is thrown when a function's argument is of an inappropriate type.
print(int('a')) #when we give wrong input


# NameError
# The NameError is thrown when an object could not be found.
print(k) #means u want to access that variable which is not created yet.


# AttributeError
L = [1,2,3]
L.upper() #list does not have upper function. Upper is function of strings

# Stacktrace