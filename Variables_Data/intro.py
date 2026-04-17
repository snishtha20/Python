# Dynamic V/s Static Typing

# Dynamic typing : you don't need to declare a variable's type before using it. The interpreter automatically determines the type based on the value assigned.
a = 5
print(a)

# Static Typing(C/C++): When the data type of a variable is decided before the program runs (at compile time). Type is decided automatically while running.
int a = 5;



# Dynamic V/s Static Binding

# Dynamic Binding: A variable can change its type while the program runs.
a = 5
print(a)

a = "Nishtha Singh"
print(a)


# Static Binding: A variable’s type is fixed at compile time and cannot change later.
int a = 5;


# Stylish declaration Techniques
a,b,c = 1,2,3
print(a,b,c)

a=b=c=5
print(a,b,c)


# Type Conversion: is a way to convert a variable from one data type to another data type
# Two types: Implicit & Explicit

# Implicit: Python changes itself
print(5+5.6) #it implicit convert data type to float
print(type(5), type(5.6))

# Explicit: Python explicit type conversion doesn't change original data it creates new data
# int(), str(), float()
n1 = input("Enter 1st no.: ")
n2= input("Enter 2nd no.: ")
result = int(n1) + int(n2)
print(result)
print(type(n1)) #str because at the line 45 int(n1) creates new data which data type is int and we are asking here data type of original n1 which is string. 
