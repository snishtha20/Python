# Find the length of a given string without using the len() function.
# s = input("Enter a string: ")
# count =0
# for i in s:
#     count+=1
# print(count)


# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh
# s = input("Enter email: ")
# pos = s.index('@')
# print(s[:pos])


# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
# s = 'hello how are you'
# term = input('what would like to search for: ')
# print(s.count(term))


# Write a program which can remove a particular character from a string.
# s = input('enter the string: ')
# term = input('what would like to remove: ')

# result = ' '
# for i in s:
#     if i != term:
#         result+=i
# print(result)


# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam
# s = 'racecar'
# flag = True
# for i in range(0, len(s)//2):
#     if s[i] != s[len(s)-i-1]:
#         flag = False
#         print("Not a palindrome")
#         break
# if flag:
#     print("Palindrome")

    
# Write a program to count the number of words in a string without split()
# s = 'My name is Nishtha Singh'
# count =0
# for i in s:
#     if i == ' ':
#         count +=1
# print('No. of words: ', count+1)


# s = 'My name is Nishtha Singh'
# L =[]
# temp = ''
# for i in s:
#     if i != ' ':
#         temp += i
#     else:
#         L.append(temp)
#         temp = ''
# L.append(temp)
# print(L)



# Write a python program to convert a string to title case without using the title()
# s = 'my name is nishtha singh'
# L = []
# for i in s.split():
#     L.append(i[0].upper() + i[1:].lower()) 
# print(" ".join(L))


# Write a program that can convert an integer to string.
num = int(input("Enter a number: "))
digits = '0123456789'
result = ''
while num !=0:

    result = digits[num%10] + result
    num = num//10
print(result)
print(type(result))