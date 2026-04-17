# Arithmetic Operators
print(5+6)
print(5-6)
print(5*6)
print(5/2)
print(5//2) #integer division: if quotient is in float then it will convert it to int. eg. 2.5 to 2
print(5**2) #power: 5 to the power 2
print(5%2) # reminder

# Relational Operators
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4!=4)


# Logical Operators
print(1 and 0)
print(1 or 0)
print(not 1) # it will give false because false =0 & true =1


# Bitwise Operators: Apply only on binary numbers
print(2 & 3) #Bitwise AND
print(2 | 3) # Bitwise OR
print(2 ^ 3) #Bitwise XOR: odd no. of 1 then 1 and even no of 1 then 0
print(~3) #Bitwise NOT
print(4 >> 2) #Left shift
print(5 << 2) #Right Shift


# Assignment Operators
a = 2
a+=2
print(a) #4
a-=2
a/=2
a%=2


# Membership operators: Works on every container data types: String, list, tuple, set, dict
# in/not in
print('D' in 'Delhi')
print('D' not in 'Delhi')
print(1 in [2,3,4,5])