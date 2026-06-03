class atm:
    # constructor
    def __init__(self):
        self.pin =''
        self.__balance= 0
        # self.menu()  
    

    # getetr & setter methods
    def get_balance(self):
        print(self.__balance)
    def set_balance(self, new_value):
        # new_value = int(input('Enter new balance: '))
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Not valid data")

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """
                           )

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
        
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input('Enter balance: '))
        self.__balance = user_balance
        print('pin created successfully')

        # self.menu()
    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print('pin changed successfully')

        else:
            print("Wrong pin")
        # self.menu()
        
    def check_balance(self):
        user_pin = input("Enter pin: ")
        if user_pin == self.pin:

            print("Your balance is: ", self.__balance)
        else:
            print("Enter correct pin")
        # self.menu()
        
    def withdraw(self):
        user_pin = input('enter the pin: ')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('enter the amount: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('withdrawl successful. Balance is',self.__balance)
            else:
                print('Not valid amount')
        else:
            print('Enter correct pin: ')
        # self.menu()

obj = atm()

# Before making balance private
# obj.create_pin()
# obj.balance = 'hehehe'
# obj.withdraw() # error 

# after making balance private , so that we can protect it's value
# obj.create_pin()
# obj.__balance = 'hehehe'
# obj.withdraw() #no error because as u make balance private, new variable/attribute created name start with class name i.e, _Atm__balance. And outside the class tha value of __balance was changing not the actual value. That's why it doesn't throw error.

# But if we direct change the value of _Atm__balance
obj.create_pin()
# obj._atm__balance = 'hehehe'
# obj.withdraw()

# So what if we make attributes private then also it's value can be changed from outside of the class. SO how can we protect them.
# But in python, nothing is truely private. We cannot make anything complete private. So why in python nothing is private? because python is a programming language build for adults not for children

# So firstly we should keep our data private not public. So all variables in class should be private so that no one can access their value.
# But in case if we want to give access of value of private variables and also do not want to make it public, then we have to use getter setter methods. 
# Concept is : If we make variables private then their value cannot access from outside of the class but can available inside the class that means rest methods of class can access private variables. So we will create methods inside the class which will show values of private variables outside of the class. So every data you have in your class, u have 2 methods: getter, setter
# Getter: use to show value outside of the class
# Setter: use to change values from outside of the class.
# we will create get_balance() and set_balance()

obj.get_balance()
obj.set_balance(1000)
# obj.withdraw()
obj.get_balance()

# what if someone changed balance to 'hehehe' so we will use if and type statement
obj.set_balance('hehehe')
obj.set_balance(500)

# Why encapsulation? Because hame hamare data ko private bhi banana hota h taki har koii access na kr sake or hame kuch logo ko uska access bhi dena hota h taki wo un private variables ka use kr sake to 
# in a protected manner we use getter & setter method 
