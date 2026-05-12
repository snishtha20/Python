# Reference Variables
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object

# object without a reference
class Person:
    def __init__(self):
        self.name = "Nishtha"
        self.gender = "Female"

p = Person()
q = p

# Multiple ref
print(id(p))
print(id(q))


# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'Mishthi'
print(q.name)
print(p.name)


# This means p holds only refrence of object. Object is created as we write Person() only. we store it's address to p so that we can use it further.
# And as we copied reference to q. q and p pointing out same memory box. So if any changes happens in q, resulting p's values will also change.

# **Pass by reference
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print('Hi my name is',person.name,'and I am a',person.gender)
  p1 = Person('ankit','male')
  return p1

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)


# 2nd
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print(id(person))
  person.name = 'ankit'
  print(person.name)

p = Person('nitish','male')
print(id(p))
greet(p)
print(p.name)


# Object ki mutability: Objects are mutable because as the q changes name of main class, ultimately value of name of p also changes
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  person.name = 'ankit'
  return person

p = Person('nitish','male')
print(id(p))
p1 = greet(p)
print(id(p1))
