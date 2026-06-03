# instance variable: An instance variable is a variable defined using self that stores object-specific data in a class
class Person:
    def __init__(self, name_input, gender_input) :
        self.name = name_input
        self.gender = gender_input

p1 = Person('Nishtha', 'female')
p2 = Person('Raj', 'male')

p2.name


