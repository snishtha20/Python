# Exceptions
# If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.

# Exceptions are raised by python runtime
# You have to takle is on the fly
# Examples
# Memory overflow
# Divide by 0 -> logical error
# Database error

# Necessity of exception-handling: 
# why we need exception handling
# 1. User Experience: Exception handling improves user experience by preventing crashes and providing meaningful feedback
# 2. Security Breach: it improves security by preventing sensitive system information from being exposed during errors.

# mostly there is risk of having errors when we open file/folder/database connection/bluetooth connection or anything else from external source.

# # let's create a file
# with open('sample.txt', 'w') as f:
#     f.write('Nishtha Singh')

# # try catch demo
# try:
#     with open('sample1.txt', 'r') as f:
#         print(f.read())
# except:
#     print('Sorry file not found')

# catching specific exception
# try:
#     with open('sample1.txt', 'r') as f:  #throws error
#         print(f.read())
#         print(m) #throws error
# except:
#     print('some error occured')

# try:
#     with open('sample.txt', 'r') as f:
#         print(f.read())
#         print(m) #throws error
# except:
#     print('some error occured')

# So if we have 2 errors in try block so we have to write 2 except block
# try:
#     with open('sample.txt', 'r') as f:
#         print(f.read())
#         print(m) 
# # below syntax of except block tells the error. it handles generic exceptions means all errors
# except Exception as e:
#     print(e.with_traceback)     


# try:
#     m =5
#     with open('sample.txt', 'r') as f:
#         print(f.read())
#         print(m) 
#         print(5/0)
#         L= [1,2,3,4]
#         print(L[100])
# # below syntax of except block is used to handle multiple errors
# except FileNotFoundError:
#     print('file not found')
# except NameError:
#     print('Variable not defined')
# except ZeroDivisionError:
#     print("can't divide by zero")
# except Exception as e:
#     print(e)       

# the last except block should use every time because if mistakenly miss any exception handle in that case, last bexcept block will handle that error.



# else
# when try block has some error then except block executes and handles that error. But when try block executes successfully then else block will execute.
# else me wo line of code likhne h jiske liye super sure ho ki isme koii error nhi aayega.
# try:
#     f = open('sample.txt', 'r')

# except FileNotFoundError:
#     print('file not found')
# except Exception:
#     print('some error occurred')

# else:
#     print(f.read())



# finally: finally block is used in exception handling to execute code regardless of whether an exception occurs or not.
# The finally block always runs, even if:
# No exception occurs
# An exception occurs and is handled

# try:
#     f = open('sample.txt', 'r')

# except FileNotFoundError:
#     print('file not found')
# except Exception:
#     print('some error occurred')

# else:
#     print(f.read())

# finally:
#     print('It will definetly print')

# Use of finally:
# 1. Resource Cleanup
# Used to close files, database connections, network sockets, bluetooth connection etc.

# 2. Better User Experience
# Ensures cleanup or final messages are shown even if an error occurs.

# 3. Security & Reliability
# Prevents resources from remaining open, which could lead to:
# Memory leaks
# Locked files
# Unreleased database connections
# System instability


# raise
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance
    
#     def withdraw(self, amount):
#         if amount < 0:
#             raise Exception("amount can't be negative")
#         if self.balance < amount:
#             raise Exception('amount is more than balance')
#         self.balance = self.balance-amount
       
# obj = Bank(10000)
# try:
#     obj.withdraw(5000) #-5000, 15000
# except Exception as e:
#     print(e)
# else:
#    print(obj.balance)


# creating custom exception: Our own exceptions
# It's uses: full control, application based errors
# Use case: It's use case is when there is possibility of mistake and u want to do some work when mistake is done.
                                                                           
# class MyException(Exception):
#     def __init__(self, message):
#         print(message)
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance
    
#     def withdraw(self, amount):
#         if amount < 0:
#             raise MyException("amount can't be negative")
#         if self.balance < amount:
#             raise MyException('amount is more than balance')
#         self.balance = self.balance-amount
       
# obj = Bank(10000)
# try:
#     obj.withdraw(15000) #-5000, 15000
# except Exception as e:
#     pass
# else:
#    print(obj.balance)

# example
class SecurityMessage(Exception):
    def __init__(self, message):
        print(message)
    def logout(self):
        print('logout')
class Google:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device!= self.device:
            raise SecurityMessage("Wrong Device!")
        if email== self.email and password == self.password:
            print("login successfuly")
        else:
            print('login error')

obj = Google('Nishtha', 'snishtha2006@gmail.com', '1234', 'android')

try:
    obj.login('snishtha2006@gmail.com', '1234', 'mac')
except SecurityMessage as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connection closed')