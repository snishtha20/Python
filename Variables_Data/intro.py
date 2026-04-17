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
