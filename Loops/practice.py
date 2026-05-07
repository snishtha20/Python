# Q.1 The current population is 10000. Population is increasing at the rate of 
#     10% per year. WAP to find out population at the end of each of last 10 years

# curr_pop = 10000
# for i in range(10, 0, -1):
#     print(i, curr_pop)
#     curr_pop = curr_pop/1.1


# Why 1.1
# let's take 9th year's population be x
#     x + 10% of x = 10000
#     x + 0.1x = 10000
#     1.1x = 10000
#     x = 10000/1.1



# Q.2 Sequence Sum: 1/1! + 2/2! + 3/3!....
n =  int(input('Enter n: '))
result =0
fact =1
for i in range(1, n+1):
    fact = fact * i
    result = result + i/fact

print(result)
