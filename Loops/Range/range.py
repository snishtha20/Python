# range() = Range functions returns a sequence of numbers, starting from 0 by default and increments by 1(by default) and stops before a specified number.
# range(start, stop?, step)

print(range(5))

seq = range(5)
print(seq)

for i in seq:
    print(i)

# 2nd
for i in range(10):              # range(stop)
    print(i)

for i in range(1,10):            # range(start, stop)
    print(i)

for i in range(1,10,2):          # range(start, stop, step)
    print(i)


