# Recursion: When a function calls itself repeatedly.

# print n to 1 
# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# show(5)

# factorial

# def fact(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)

# result = fact(5)
# print(result)


# Practice

# Sum of first n num
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# result = sum(5)
# print(result)

# print all elements in a list
def print_list(list, i):
    if i == len(list):
        return
    else:
        print(list[i])
        print_list(list, i+1)

print_list(["a", "b", "c", "d"], 0)