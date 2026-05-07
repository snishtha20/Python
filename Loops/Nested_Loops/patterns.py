# Pattern 1
# rows = int(input("Enter number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1, i+1):
#         print("*", end=' ')
#     print()

# Pattern 2
# rows = int(input("Enter number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# Pattern 3
# rows = int(input("Enter number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1, i+1):
#         print(i, end=' ')
#     print()



# Pattern 4
rows = int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    for k in range(i-1, 0, -1):
        print(k, end=' ')
    print()   