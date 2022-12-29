import math


def func(x, y):
    return 3 * x * x + 4 * x * y + y * y - 8 * x - 12 * y


def func1(x, y):
    return 6 * x + 4 * y - 8


def func2(x, y):
    return 4 * x + 2 * y - 12


def gradient(x1, x2, lamb, e):
    func_ = 999
    res = 0
    while True:
        res += 1
        print("Lan thu ", res)
        print("X(0) = ", "%.5f" % x1, " ; ", "%.5f" % x2)
        print("f[X(0)] = ", "%.5f" % func(x1, x2))
        print("Gradient f[X(0)] = (", "%.5f" % func1(x1, x2), " ; ", "%.5f" % func2(x1, x2), ")")

        x1_ = x1
        func_ = func(x1, x2)
        x1 = x1 + lamb * func1(x1, x2)
        x2 = x2 + lamb * func2(x1_, x2)
        if abs(func(x1, x2) - func_) < e:
            break
        print("|f(Xi+1)-f(Xi)| = ", "%.5f" % abs(func(x1, x2) - func_))
        func_ = func(x1, x2)


x1 = 0
x2 = 0
lamb = 0.25
e = 0.05
gradient(x1, x2, lamb, e)
