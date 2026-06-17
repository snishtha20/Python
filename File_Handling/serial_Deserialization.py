# Serialization and Deserialization
# Serialization - process of converting python data types to JSON format
# Deserialization - process of converting JSON to python data types

# JSON format (JavaScript On Notation): it is universal data format. Every programming language understands this format. Every API use json format. It's structure like dictionary format like it have key-value pairs.


# serialization using json module
# # list
# import json 

# L=[1,2,3,4]

# with open('demo.json', 'w') as f:
#     json.dump(L, f)

# # dict
# d = {
#     'name':'Nishtha',
#      'age':21,
#      'gender':'female'
# }
# with open('demo.json', 'w') as f:
#     json.dump(d, f, indent=4) #indent =4 because 1 tab space = 4spaces

# deserialization
# import json

# with open('demo.json', 'r') as f:
#     d= json.load(f)
#     print(d)
#     print(type(d))


# serialize and deserialize tuple: tuple can't be serialize & deserialize, if we want to write tuple in json file then it will automatically convert to list.
# import json

# t= (1,2,3,4)

# with open('demo.json', 'w') as f:
#     json.dump(t, f)


# serialize and deserialize a nested dict
# import json 

# d = {
#     'student': "Nishtha",
#     'marks':[1,2,3,4,5]
# }

# with open('demo.json', 'w') as f:
#     json.dump(d, f)


# Serializing and Deserializing custom objects
class Person:

  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

# format to printed in
# -> Nishtha Singh age -> 21 gender -> female

person =Person("Nishtha", "Singh", 21, 'female')

# As a string
# import json

# with open('demo.json', 'w') as f:
#   json.dump(person, f) #will throw error. to serialize objects, there is a different way.

# As a string
# import json

# def show_object(person):
#   if isinstance(person, Person):
#     return "{} {} age -> {} gender -> {}".format(person.fname, person.lname, person.age, person.gender)

# with open('demo.json', 'w') as f:
#   json.dump(person, f, default= show_object)

# As a dictionary
import json

def show_object(person):
  if isinstance(person, Person):
    return {'name' : person.fname + ' ' + person.lname, 'age' : person.age, 'gender': person.gender}

with open('demo.json', 'w') as f:
  json.dump(person, f, default= show_object, indent =4)

# deserializing
import json

with open('demo.json', 'r') as f:
  d=json.load(f)
  print(d)
  print(type(d))

# But what if we want to serialize object as it is and deserialize the same object. So that we can perform all functions which we performs on normal object
# We cannot serialize and deserialize objects of class in this way. We'll use Pickling for this.