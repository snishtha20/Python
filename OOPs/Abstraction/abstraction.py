# Abstraction: it means hiding unnecessary details and display important details
# mandatory to use @abstractmethod decorator and it's code should be written in inherited method.
from abc import ABC,abstractmethod 
class BankApp:
    def database(self):
        print('connected to datbase')
    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print('login into mobile')
    def security(self):
        print('mobile security')
