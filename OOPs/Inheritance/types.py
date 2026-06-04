# Types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Multiple Inheritance(Diamond Problem)
# Hybrid Inheritance


# single inheritance : 1 parent, 1 child
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()


# multilevel: 1 grandparent, 1 parent, 1 child
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()


# Hierarchical: 1 parent, multiple child
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()


# Multiple: multiple parents, 1 child
# Example 1
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")


class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy() 
s.review()


# Example 2
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# Method resolution order
class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy() # konse parent ka buy method call hoga? jo smartphone ne sabse pahle inherit kiya i.e Phone {SmartPhone(Phone, Product)}, if we change order then buy method of another parent(i.e Product) will call, this is called as Method resolution order.



# Practice questions
# 1
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
  
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1() + obj3.m1()+ obj3.m2()) #70


# 2
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val=super().m1()+30
        return val

class C(B):
  
    def m1(self):
        val=self.m1()+20
        return val
obj=C()
print(obj.m1()) #will throw RecursionError because self.m1() call itself(m1 method) repeatedly and it becomes infinite loop. it won't call m1 mthod of class B because self keyword means ussi class ka method call hoga