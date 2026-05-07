# Creating Strings
s = 'hello'
s = "hello"
#for multiple lines
s = '''hello''' 
s = """hello"""
s =str('hello')
print(s)


# Accessing Strings
# Positive Indexing
s = 'hello world'
print(s[1])
# Negative Indexing: it's use when u don't know the length of string still u can extract last element of string
s = 'hello world'
print(s[-1])


# Slicing
s = 'hello world'
print(s[0,5])
print(s[::-1])
print(s[-1:-6:-1])


# Adding Chars to Strings 
# Editing Strings: Python Strings are immutable
# Deleting Strings
s = 'hello world'
del s
print(s) #error: name 's' is not found
s = 'hello world'
del s[-1:-5:2]
print(s) #throw error because in python strings are immutable so can't modify in any way


# Operations on Strings
# Arithmetic Operations
print('delhi' + 'mumbai') #delhimumbai
print('delhi' * 5) #delhidelhidelhidelhidelhi

# Relational Operations
'delhi' == 'delhi' #true
'delhi' != 'delhi' #false
'mumbai' > 'pune' #false because it checks lexiographically means according to ASCII- Jaise ABCD me P baad me aata h to wo bada maana jata h
'Pune' > 'pune' #Capital letters ki ASCII Value kam hoti h small se

# Logical Operations
# In python, empty string considered as False
" " or 'world' #world
" " and 'world' #" "

'hello' and 'world'  #world: because for and, both must true so python has to check 2nd string also to get true so it gives 2nd string in result
'hello' or 'world' #hello: because for or, only one must true so as it gets true in 1st string it don't traverse forward and gives 1st string in reuslt

not " " #True
not "hello" #False

# Loops on Strings
for i in 'hello':
    print(i)

for i in 'delhi':
    print('pune')


# Membership Operations
'D' in 'Delhi' #True
'D' not in 'Delhi' #False
'D' in 'delhi' #False


# String Functions
len("hello world") #11 include space
max("hello world") #w according to ASCII Values
min("hello world") #' ' space has lowest ASCII Value
sorted("hello world") 
sorted("hello world", reverse=True) #['w', 'r', 'o', 'o', 'l','l','l','h','e','d',' ']









str = "i am a coder"

print(str.endswith("er"))
print(str.capitalize())
print(str.replace("coder", "programmer"))
print(str.find("am")) #return index of 1st occurence
print(str.count("a"))

# 1. Case Conversion Methods
# | Method             | Description                                 | Example                                        |
# | ------------------ | ------------------------------------------- | ---------------------------------------------- |
# | `str.upper()`      | Converts all characters to uppercase        | `"hello".upper()` → `'HELLO'`                  |
# | `str.lower()`      | Converts all characters to lowercase        | `"HELLO".lower()` → `'hello'`                  |
# | `str.capitalize()` | Capitalizes first character                 | `"hello world".capitalize()` → `'Hello world'` |
# | `str.title()`      | Capitalizes first letter of each word       | `"hello world".title()` → `'Hello World'`      |
# | `str.swapcase()`   | Swaps uppercase to lowercase and vice versa | `"Hello World".swapcase()` → `'hELLO wORLD'`   |


# 2. Searching and Checking Methods
# | Method                   | Description                                            | Example                             |
# | ------------------------ | ------------------------------------------------------ | ----------------------------------- |
# | `str.find(sub)`          | Returns lowest index of substring or `-1` if not found | `"hello".find("l")` → `2`           |
# | `str.rfind(sub)`         | Returns highest index of substring or `-1`             | `"hello".rfind("l")` → `3`          |
# | `str.index(sub)`         | Like `find()`, but raises `ValueError` if not found    | `"hello".index("e")` → `1`          | #index and find is same only difference is find generates -1 in case no element is found but index generate error
# | `str.rindex(sub)`        | Like `rfind()`, but raises `ValueError` if not found   | `"hello".rindex("l")` → `3`         |
# | `str.startswith(prefix)` | Checks if string starts with prefix                    | `"hello".startswith("he")` → `True` |
# | `str.endswith(suffix)`   | Checks if string ends with suffix                      | `"hello".endswith("lo")` → `True`   |
# | `str.isalpha()`          | Returns `True` if all characters are letters           | `"Hello".isalpha()` → `True`        |
# | `str.isdigit()`          | Returns `True` if all characters are digits            | `"123".isdigit()` → `True`          |
# | `str.isalnum()`          | Returns `True` if all characters are letters/digits    | `"abc123".isalnum()` → `True`       |
# | `str.islower()`          | Returns `True` if all letters are lowercase            | `"hello".islower()` → `True`        |
# | `str.isupper()`          | Returns `True` if all letters are uppercase            | `"HELLO".isupper()` → `True`        |
# | `str.isspace()`          | Returns `True` if all characters are whitespace        | `"   ".isspace()` → `True`          |
# | `str.isnumeric()`        | Returns `True` if all characters are numeric           | `"123".isnumeric()` → `True`        |
# | `str.isdecimal()`        | Returns `True` if all characters are decimal           | `"123".isdecimal()` → `True`        |
# | `str.isidentifier()`     | Checks if string is a valid Python identifier          | `"var1".isidentifier()` → `True`    |


# 3. Modification / Formatting Methods
# | Method                           | Description                                      | Example                                     |
# | -------------------------------- | ------------------------------------------------ | ------------------------------------------- |
# | `str.strip([chars])`             | Removes leading and trailing whitespace or chars | `"  hello  ".strip()` → `'hello'`           |
# | `str.lstrip([chars])`            | Removes leading whitespace or chars              | `"  hello".lstrip()` → `'hello'`            |
# | `str.rstrip([chars])`            | Removes trailing whitespace or chars             | `"hello  ".rstrip()` → `'hello'`            |
# | `str.replace(old, new[, count])` | Replaces old substring with new one              | `"hello".replace("l", "x")` → `'hexxo'`     |
# | `str.center(width[, fillchar])`  | Centers string in width with optional fill char  | `"hello".center(11, "-")` → `'---hello---'` |
# | `str.ljust(width[, fillchar])`   | Left-justifies string                            | `"hello".ljust(10, "*")` → `'hello*****'`   |
# | `str.rjust(width[, fillchar])`   | Right-justifies string                           | `"hello".rjust(10, "*")` → `'*****hello'`   |
# | `str.zfill(width)`               | Pads string on the left with zeros               | `"42".zfill(5)` → `'00042'`                 |
# | `str.expandtabs(tabsize=8)`      | Replaces `\t` with spaces                        | `"a\tb".expandtabs(4)` → `'a   b'`          |


# 4. Other Useful Methods
# | Method                           | Description                                         | Example                                                                 |
# | -------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------- |
# | `str.count(sub[, start[, end]])` | Counts occurrences of substring                     | `"hello".count("l")` → `2`                                              |
# | `str.partition(sep)`             | Splits string at first occurrence of sep into tuple | `"hello world".partition(" ")` → `('hello', ' ', 'world')`              |
# | `str.rpartition(sep)`            | Splits string at last occurrence of sep             | `"hello world hello".rpartition(" ")` → `('hello world', ' ', 'hello')` |
# | `str.format(*args, **kwargs)`    | Formats string using placeholders                   | `"Hello {}".format("Alice")` → `'Hello Alice'`                          |
# | `str.removeprefix(prefix)`       | Removes prefix if present (Python 3.9+)             | `"HelloWorld".removeprefix("Hello")` → `'World'`                        |
# | `str.removesuffix(suffix)`       | Removes suffix if present (Python 3.9+)             | `"filename.txt".removesuffix(".txt")` → `'filename'`                    |


# More functions
# 1. split
'hi my name is Nishtha'.split() #['hi', 'my', 'name', 'is', 'Nishtha']
'hi my name is Nishtha'.split('i') #['h', 'my name', 's N', 'shtha']

# 2. join
" ".join(['hi', 'my', 'name', 'is', 'Nishtha']) #'hi my name is Nishtha'
"-".join(['hi', 'my', 'name', 'is', 'Nishtha']) #'hi-my-name-is-Nishtha'

# 3. replace
'hi my name is Nishtha'.replace('Nishtha', 'Mishthi') #'hi my name is Mishthi'


# Every function genrating new string with required changes. No changes happens in original string