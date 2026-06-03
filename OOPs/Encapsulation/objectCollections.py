# Collections of object

# # List of objects
# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
    
# p1 = Person('Nishtha', 'female')
# p2 = Person('Anish', 'male')
# p3 = Person('Deepika', 'female')

# L = [p1,p2,p3]
# print(L) #Address of every object will print because we didn't use str function to represent them

# # loop on list
# for i in L:
#     # print(i)    
#     print(i.name, i.gender) # i.name isiliye possible hua kyuki object me . use krke uske attribute ko access kr skte h



# Dictionary of objects
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender      

p1 = Person('Nishtha', 'female')
p2 = Person('Anish', 'male')
p3 = Person('Deepika', 'female')

d = {'p1': p1,
     'p2': p2,
     'p3': p3}

for i in d:
    # print(i, d[i])
    print(d[i].name)
    print(d[i].gender)
    