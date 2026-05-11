# def sum(a,b):
#     return a+b

# sum = sum(2,3)
# print(sum)

# # 2nd
# def hello():
#     print("Hello Nishtha!")

# hello()

# # 3rd 
# def hello():
#     print("hello")

# output = hello()
# print(output)  #None because there is no return statement in function block

# Conclusion: if we use return statement then we have to call the function by declaring/storing a new variable  

# if we did not use return statement in function then the value of return statement will be: None
# L = [1,2,3]
# print(L.append(4)) #None because this function does not return anything it only adds element in the end of list.
# print(L)

# 4th Avg of 3 numbers
# def avg(a,b):
#     print("Average: ", (a+b)/2)

# avg(4,6)


# # OR

# def avg(a,b):
#     return (a+b)/2

# output = avg(4,6)
# print("Average: ", output)


# 5th even/odd
def is_even(num):
    # below block of code is called as docstring
    """ 
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 16th Nov 2022
    """

    if type(num) == int:
        if num%2==0:
            return "Even"
        else:
            return "Odd"
        
    else:
        return "Wrong datatype"
    
for i in range(1,11):
    x = is_even(i)
    print(x)

print(is_even.__doc__) #way to print documentaion(docstring)