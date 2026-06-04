# Method overriding: if both parent & child class have method with same name then child's method will call. If we create parent class's object then only we can call parent's method
# Constructor overriding: if parent and child class both have constructor then child's constructor will call, shown in inherited.py
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()