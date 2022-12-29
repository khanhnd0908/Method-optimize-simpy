import math


def func(x):
    return x * x + x + math.sin(x)


def GoldenSectionMethod(a, b, e):
    while 2 * e < (b - a):
        # Find 2 bounded points
        x1 = a + 0.382 * (b - a)
        x2 = a + 0.618 * (b - a)

        # Calculate value of xi
        y1 = func(x1)
        y2 = func(x2)

        # Check if middle point is extreme
        if y1 < y2:
            b = x2
        else:
            a = x1

    c = (a + b) / 2
    print("The optimal value of function f_min = ", "%.5f" % func(c), " at the point x = ", "%.5f" % c)


a = -1
b = 0
e = 0.003
GoldenSectionMethod(a, b, e)
