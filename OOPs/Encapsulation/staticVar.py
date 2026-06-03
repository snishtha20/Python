# Static Variable: a static variable usually means a class variable—a variable that belongs to the class itself rather than to individual objects.
# A static (class) variable is a variable declared inside a class but outside its methods. It is shared by all objects of the class and occupies memory only once regardless of how many objects are created.
# Diff b/w instance & static variable :
# Instance is object varaible means belongs to object whereas Static is class varaible means it belongs to class
# Instance variable's value is separate copy for each object means object have separate values whereas Static variable's value shared to all objects means all objects have same value 
# Accessed with: Instance: self.varName  & Static: className.varName 
# Instance variables always defined inside constructor whereas static variables defined outside of all the methods

# Rule to remember
# Inside __init__():
# atm.counter = value → modifies the static/class variable.
# self.counter = value → creates or modifies an instance variable for that object.


class atm:
    __counter = 1
    # constructor
    def __init__(self):
        self.pin =''
        self.__balance= 0
        self.cid = atm.__counter
        atm.__counter = atm.__counter + 1
        # self.menu()  

    # utiliy functions: means they don't need any object
    @staticmethod #this is static method we can directly access/call this method without even creating any object by just using class name. it's use to create utility functions
    def get_counter():     # we won't use self because it is not accessing value by object name
        print(atm.__counter)
    
    # getter & setter methods
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

# c1 = atm()
# c2 = atm()
# c3= atm()
# print(c1.cid)
# print(c2.cid)
# print(c3.cid)
# print(atm.counter)

# what if someone changed static variable's value incorrectly
# atm.counter = 'hehehe'
# c1 = atm() #throw error

# so we have to make it private but if we make it private and someone really wants to access it then? So we
# will also create getter setter methods for static variables. Yes we can do the same for static variables also and these are
# called as Static methods and way to call these methods by using class name not objectname i.e, atm.get_counter() not c1.get_counter()

print(atm.get_counter())
