# Pickling
# Pickling is the process whereby a Python object hierarchy is converted into a byte stream(binary file), 
# and unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) 
# is converted back into an object hierarchy.

class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display_info(self):
    print('Hi my name is',self.name,'and I am ',self.age,'years old')

p = Person('Nishtha', 21)

# pickle dump
import pickle
with open('person.pkl', 'wb') as f:
  pickle.dump(p, f)

# pickle load

with open('person.pkl', 'rb') as f:
  p = pickle.load(f)

p.display_info()

# Pickle Vs Json
# Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format
# Pickle is used when you want to retain the functionality of object. JSON is used when you want to display object in text format, but object will get lost means it won't have same functionality as the original object owns.
# Pickle is used when you have created the class in one machine and want to use it's object on other machine/system.