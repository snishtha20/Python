# Working with mathematical formulas
import numpy as np

# built-in functions
# a=np.arange(10)
# print(np.sum(a))
# print(np.sin(a))

# user defined
# sigmoid
# def sigmoid(a):
#     print(1/(1+np.exp(-a)))

# a=np.arange(10)
# sigmoid(a)

# Mean Squared Error
# actual = np.random.randint(1,10,8)
# predicted = np.random.randint(1,10,8)

# def mse(a,p):
#     print(np.mean((a-p)**2))

# mse(actual, predicted)

# Binary cross entropy
# def bce(y, p):
#     print(np.mean(-(y * np.log(p) + (1-y) * np.log(1-p))))

# bce(1, 0.80)


### Working with missing values
# Working with missing values -> np.nan
a = np.array([1,2,3,4, np.nan, 6])
print(a)
print(a[~np.isnan(a)])

