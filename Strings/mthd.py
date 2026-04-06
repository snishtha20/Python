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
# | `str.index(sub)`         | Like `find()`, but raises `ValueError` if not found    | `"hello".index("e")` → `1`          |
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
