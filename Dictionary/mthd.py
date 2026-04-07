myDict = {
    "name" : "Nishtha Singh",
    "branch" : "CSE",
    "year" : 3,
    "sem" : 6
}

# print(myDict)
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
# print(myDict.get("branch"))
# print(myDict['branch'])

# newDict = {
#     "cgpa" : 8.59
# }
# myDict.update(newDict)
# print(myDict)


# why we use .get method to get value of corresponding key while we can get it by simply print(myDict["branch"])

# print(myDict["name2"]) #error
# print("hi")
# print("Nishtha")
# print("I'm a coder")

# print(myDict.get("name2")) #None
# print("hi")
# print("Nishtha")
# print("I'm a coder")



# All Python Dictionary Methods

# 1. Adding & Updating
# dict.update()
# Updates dictionary with key-value pairs from another dict
# d = {'a': 1, 'b': 2}
# d.update({'b': 3, 'c': 4})
# # {'a': 1, 'b': 3, 'c': 4}

# dict.setdefault(key, default)
# Returns value of key; if not present, inserts key with default value
# d = {'a': 1}
# d.setdefault('b', 2)
# # {'a': 1, 'b': 2}

# 2. Removing Elements
# dict.pop(key[, default])
# Removes and returns value of key
# d = {'a': 1, 'b': 2}
# d.pop('a')
# # returns 1 → {'b': 2}

# dict.popitem()
# Removes and returns last inserted key-value pair
# d = {'a': 1, 'b': 2}
# d.popitem()
# # ('b', 2)

# dict.clear()
# Removes all items
# d = {'a': 1}
# d.clear()
# # {}


# 3. Accessing Elements
# dict.get(key[, default])
# Returns value of key (no error if missing)
# d = {'a': 1}
# d.get('b', 0)   # 0

# dict.keys()
# Returns all keys
# d = {'a': 1, 'b': 2}
# d.keys()   # dict_keys(['a', 'b'])

# dict.values()
# Returns all values
# d.values()   # dict_values([1, 2])

# dict.items()
# Returns key-value pairs
# d.items()   # dict_items([('a', 1), ('b', 2)])


# 4. Copying
# dict.copy()
# Returns shallow copy
# d = {'a': 1}
# new_d = d.copy()


# 5. Creating Dictionaries
# dict.fromkeys(iterable, value)
# Creates dictionary with given keys and same value
# keys = ['a', 'b', 'c']
# d = dict.fromkeys(keys, 0)
# # {'a': 0, 'b': 0, 'c': 0}


# Important Points (Exam + Interview)
# Dictionaries are:
# Mutable
# Store data in key-value pairs
# Keys must be unique & immutable
# get() is safer than []:



# Bonus (Useful Functions with Dictionary)
# len(d)      # number of items
# type(d)     # dict



# 🔥 Quick Trick to Remember
# CRUD Operations:
# Create → fromkeys()
# Read → get(), keys(), values(), items()
# Update → update(), setdefault()
# Delete → pop(), popitem(), clear()