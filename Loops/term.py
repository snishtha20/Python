# break: used to terminate the loop when encountered.

# i = 0
# while i<=5:
#     if(i == 3):
#         break
#     print(i)
#     i+=1

# continue: terminates execution in the current iteration & continue execution of the loop with the next iteration
# simple meaning: skip
# tip: continue se pahle hi next iteration ke liye likhna padega
i = 0
while i<=5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1
