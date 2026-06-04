# Polymorphism
# Method Overriding
# Method Overloading
# Operator Overloading

# Method overriding: if parent and child class have method with same name, and if we call that method which one execute? child class's method will execute


# Method overloading: 2 methods with same name but differ in arguments. 2 method same h but unke output different h and outputs are based on inputs 
# it's uses is to make code more cleaner so that code readability increases.
# class Shape:
#     def area(self, a):
#         print(3.14 * a *a)
#     def area(Self, l,b):
#         print(l*b)

# s= Shape()
# print(s.area(2))
# print(s.area(3,4))

# But python does not allow method overloading because it has another way to do this.
class Shape:
    def area(self, a, b=0):
        if b==0:
            print(3.14 * a *a)
        else:
            print(a*b)
s= Shape()
s.area(2)
s.area(3,4)

        

# Operator Overloading : one operator is used for multiplie purpose. implementation is magic methods. Best example is Fraction.py
print('hello' + 'world') #concatenating
print(4 + 5) #adding
print([1,2,3] + [4,5]) #merging
