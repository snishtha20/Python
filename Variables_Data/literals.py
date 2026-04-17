# Literals: these are values/constant which are assigned to variables

a = 0b1010 #Binary Literals
b = 1000 #Decimal Literals
c = 0o310 #Octal Literals
d = 0x12c #Hexadecimal Literals

print(a, b, c, d)

# Float Literal
float_1 = 10.5
float_2 = 1.5e2 #1.5 * 10^2
float_3 = 1.5e-3 #1.5 * 10^-3

print(float_1, float_2, float_3)


# Complex Literal
x = 3.14j
print(x.real, x.imag)


s1 = 'Nishtha Singh'
s2 = "Nishtha Singh"
char = "N"
multiline_str = """I'm Nishtha Singh."""
unicode = u"\U0001f600" #used for emoji
raw_str = r"raw \n string"
print(s1, s2, char, multiline_str, unicode, raw_str)
