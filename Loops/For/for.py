# list = [1,2,5,7,4,7]
# for el in list:
#     print(el)

# tup = ("hi", "hello", "hey")
# for word in tup:
#     print(word)

# str ="NishthaSingh"
# for char in str:
#     print(char)



# else

# nums = [1,2,3,4]
# for val in nums:
#     print(val)
# else:
#     print("END")

# nums = [1,2,3,4]
# for val in nums:
#     print(val)
# print("END")

# in both cases END will print then what is the use of else?

str ="NishthaSingh"
for char in str:
    if(char == 'a'):
        print("a found")
        break
    # print(char)
else:
    print("END")


str ="NishthaSingh"
for char in str:
    if(char == 'a'):
        print("a found")
        break
    # print(char)

print("END")  

# The reason behind this is if we want END will print only when loop traverse whole string then we use else
# outer statement of loop will print in every case rather the whole string traversed or not  