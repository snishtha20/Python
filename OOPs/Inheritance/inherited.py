
# What gets inherited?
# Constructor
# Non Private Attributes
# Non Private Methods


# 1. Constructor
# Remember: 
# a) if child class doesn't have it's own constructor then parent class's constructor will call.
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 13)
s.buy()


# b) if child class has it's own constructor then parent's constructor will not call and it's attribute will not initialize so child class's objct can not access parent class's instance variables. we have power to access them but this time it is not allwoing to access them because that code(parent class's constructor) did not executed
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
s.brand


# c) child can't access private members and methods of the class. Only way to access by using getter method
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s=SmartPhone(20000, "Apple", 13)
s.show()


# Example 1
class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def show(self):
        print("This is in child class")
        
son=Child(100)
print(son.get_num())
son.show()


# Example 2
class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
        
son=Child(100,10)
print("Parent: Num:",son.get_num())
print("Child: Val:",son.get_val())



# Example 3
class A:
    def __init__(self):
        self.var1=100

    def display1(self,var1):
        #will print 100 because var1 and self.var1 are different if we write 
        # self.var1 = var1 then only 200 print
        print("class A :", self.var1) 
class B(A):
  
    def display2(self,var1):
        print("class B :", self.var1)

obj=B()
obj.display1(200) 