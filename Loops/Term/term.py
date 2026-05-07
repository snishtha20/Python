# break: used to terminate the loop when encountered.
# Real life example: When searching for a person's credentials in database. Because as we will find that person there is no need to traverse loop on whole database.
# i = 0
# while i<=5: 
#     if(i == 3):
#         break
#     print(i)
#     i+=1

# for i in range(1,10):
#     if(i==5):
#         break
#     print(i)
        

# Q. Print prime numbers between 10 to 100
# start = int(input("Enter starting value: "))
# end = int(input("Enter ending value: "))
# for i in range(start, end+1):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# continue: terminates execution in the current iteration & continue execution of the loop with the next iteration
# simple meaning: skip
# tip: continue se pahle hi next iteration ke liye likhna padega

# Real life example: in e-commerce website we have tpo skip products which are out of stock

# i = 0
# while i<=5:
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i+=1


for i in range(1,10):
    if i==5:
        continue
    print(i)