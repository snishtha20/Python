def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')

f()
# infinite loop


def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
# in g(x): x = 4


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)
# in g(x): x = 4
# in h(x): x = 5
# 3
# 4
