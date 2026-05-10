d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# pop
#d.pop(3)
#print(d)

# popitem
#d.popitem()
# d.popitem()
# print(d)

# del
#del d['name']
#print(d)

# clear
d.clear()
print(d)

s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
del s['subjects']['maths']
print(s)