import math

def f(x):
    return x * x + x + math.sin(x)

def f_(x):
    return 2 * x + 1 + math.cos(x)

def f__(x):
    return 2 - math.sin(x)

def NewtonMethod(a, b):
    x1 = -2

    while abs(f_(x1) <= e):
        x0 = x1
        x1 = x0 - (f_(x0) / f__(x0))

    print("The optimal value of function f_min = ", "%.4f" % f(x1), " at the point x = ", "%.4f" % x1)

a = -1
b = 0
e = 0.003
NewtonMethod(a, b)
