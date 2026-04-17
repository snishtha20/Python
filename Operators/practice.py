# Sum of each digit of given number
number = int(input("Enter a 3 digit number: "))

# 345%10 -> 5
a = number%10

# 345//10 = 34
number = number//10

# 34%10 -> 4
b = number%10

# 34//10 ->3
number = number//10

print(a+b+number)