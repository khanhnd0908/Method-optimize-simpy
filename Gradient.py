import math


def func(x1, x2):
    return math.exp(-2 * x1 * x1 - 5 * x2 * x2 + x1 * x2)


def func1(x1, x2):
    return (-4 * x1 + x2) * math.exp(-2 * x1 * x1 - 5 * x2 * x2 + x1 * x2)


def func2(x1, x2):
    return (-10 * x2 + x1) * math.exp(-2 * x1 * x1 - 5 * x2 * x2 + x1 * x2)


def gradient(x1, x2, lamb, e):
    res = 0
    while True:
        x1_ = x1
        func_ = func(x1, x2)
        x1 = x1 + lamb * func1(x1, x2)
        x2 = x2 + lamb * func2(x1_, x2)

        res += 1
        print(res, ": ", "|f(Xi+1)-f(Xi)| = ", "%.5f" % abs(func(x1, x2) - func_), "f(X) = " "%.5f" % func(x1, x2))

        if abs(func(x1, x2) - func_) < e:
            break


x1 = -1
x2 = 0
lamb = 0.1
e = 0.0005
gradient(x1, x2, lamb, e)
