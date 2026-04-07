# print()
# print function has 2 things sep: which separated 2 words by space and end: \n which change the line
print("Nishtha","Singh") #give space automatically
# will print in separate lines
print("Hii")
print("Nishtha")
# if we want to print in same line
print("Hii", end=" ")
print("Nishtha")
# len(list)
# type()
# range()


# Default Parameters: Assigning a default value to paramter, which is used when no argument is passed.
def sum(a=1,b=1):
    print(a+b)
sum()

def sum(a,b=1):
    print(a+b)
sum(2)

# throw error
def sum(a=1,b):
    print(a+b)
sum(2)