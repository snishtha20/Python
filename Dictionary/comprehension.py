# Dictionary Comprehension
# {key: value for vars in iterable}

# print 1st 10 numbers and their squares
# print({i:i**2 for i in range(1,11)})

# using existing dict
# distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
# print({key:value*0.62 for (key,value) in distances.items()} ) #distance.items will generate every item(key-value pair) as a tuple

# using zip
# days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
# print({i:j for (i,j) in zip(days, temp_C)})

# using if condition
# products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
# print({key:value for (key,value) in products.items() if value>0})

# Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})