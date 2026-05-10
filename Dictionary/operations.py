# Dictionary Operations
# Membership
# Iteration

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
print(s)

print('name' in s)



d = {'name':'nitish','gender':'male','age':33}

for i in d:
  print(i,d[i])