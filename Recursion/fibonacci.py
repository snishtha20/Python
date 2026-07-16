# import time
# def fib(m):
#     if m==0 or m==1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)

# start = time.time()
# print(fib(12))
# print(time.time()-start)

# Above code taking too much time to execute for large input because some computations repeating so it becomes inefficient

# So to reduce execution time by using dictionary, it will store values which are computed once.  we will use large memory and use the concept of memoization

import time
def memo(m, d):

    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1, d) + memo(m-2 ,d)
        return d[m]

d = {
    0:0,
    1:1
}
start = time.time()
print(memo(12, d))
print(time.time()- start)

