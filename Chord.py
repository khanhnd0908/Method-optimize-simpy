import math

def f(x):
    return x * x + x + math.sin(x)

# First derivative function
def f_(x):
    return 2 * x + 1 + math.cos(x)

def chord(a, b):
    while True:
        x = a - (f_(a) / (f_(a) - f_(b))) * (a - b)
        if f_(x) > e:
            a = x
        elif f_(x) < -e:
            b = x
        else:
            break
    c = (a + b) / 2
    print("The optimal value of function f_min = ", "%.5f" % f(c), " at the point x = ", "%.5f" % c)

a = -1
b = 0
e = 0.003
chord(a, b)
