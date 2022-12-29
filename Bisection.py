# Python program for implementation
# of Bisection Method for
# finding optimal value

# The function is x^2 + x + sin(x)
import math


def func(x):
    return x * x + x + math.sin(x)


def bisection(a, b, e):
    while (b - a) > 2 * e:

        # Find 2 bounded points
        x1 = (a + b - e) / 2
        x2 = (a + b + e) / 2

        # Calculate value of yi
        y1 = func(x1)
        y2 = func(x2)

        # Check if middle point is optimal point
        if y1 > y2:
            a = x1
        else:
            b = x2

    c = (a + b) / 2
    print("The optimal value of function f_min = ", "%.5f" % func(c), " at the point x = ", "%.5f" % c)


# Initial values assumed
a = -1
b = 0
e = 0.003
bisection(a, b, e)
