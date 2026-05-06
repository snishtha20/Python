# Practice 1 Login Page
# email = 'nishtha123@gmail.com'
# password = '1234'
# a = input("Enter email: ")
# b = input("Enter password: ")

# if email== a and password == b:
#     print("Welcome")

# elif email != a:
#     print("Incorrect Email")
#     a = input("Enter Email: ")
#     if(a == email):
#         b = input("Enter password: ")        
#     else:
#         print("Incorrect Email")

# elif email == a and password != b:
#     print("Incorrect Password")
#     b = input("Enter password: ")
#     if(b == '1234'):
#         print("Welcome, finally!")
#     else:
#         print("Incorrect Password")

# else:
#     print("Incorrect Credentials")


# Min of 3 numbers
# a = int(input("Enter 1st no.: "))
# b = int(input("Enter 2nd no.: "))
# c = int(input("Enter 3rd no.: "))

# if a<b and a<c:
#     print("a is minimum")
# elif b<c:
#     print("b is minimum")
# else:
#     print("c is minimum")


# Menu Driven Program / Calculator
a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))

op = input(("Enter the operation: "))

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
else:
    print(a/b)