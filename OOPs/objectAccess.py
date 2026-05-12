class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'India':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)


# how to access attributes
p = Person('Nishtha', 'India')
print(p.name)
print(p.country)

# how to access methods
p.greet()

# what if i try to access non-existent attributes
print(p.gender) #throw error

 
# Attribute creation from outside of the class
p.gender = 'female'
print(p.gender)