# Create Dictionary
# empty dictionary
d = {}
print(d)

# 1D dictionary
d1 = { 'name' : 'nitish' ,'gender' : 'male' }
print(d1)

# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
print(d2)

# 2D dictionary -> JSON
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

# using sequence and dict function
d4 = dict([('name','nitish'),('age',32),(3,3)])
print(d4)

# duplicate keys
d5 = {'name':'nitish','name':'rahul'}
print(d5) #will give rahul because it's value will update to rahul

# mutable items as keys
d6 = {'name':'nitish',(1,2,3):2}
print(d6)