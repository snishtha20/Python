class atm:
    def __init__(self):
        self.pin =''
        self.balance=0
        self.menu()
    
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
        self.balance = user_balance
        print('pin created successfully')

        self.menu()
    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print('pin changed successfully')

        else:
            print("Wrong pin")
        self.menu()
        
    def check_balance(self):
        user_pin = input("Enter pin:")
        if user_pin == self.pin:

            print("Your balance is ", self.balance)
        else:
            print("Enter correct pin")
        self.menu()
        
    def withdraw(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdrawl successful. Balance is',self.balance)
            else:
                print('Not valid amount')
        else:
            print('Enter correct pin: ')
        self.menu()

obj = atm()