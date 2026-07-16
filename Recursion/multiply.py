def multiply(a,b):
    for i in range(b):
        if b == 1:
            return a
        else:
            return a + multiply(a, b-1)
        
s = multiply(4,5)
print(s)