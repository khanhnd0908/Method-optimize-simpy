import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * x + x + np.sin(x)


def printFunc(f, a, b, x, y):
    t = np.arange(a, b, 0.01)
    s = f(t)
    plt.plot(t, s)
    plt.plot([x], [y], 'ro')
    plt.show()


def search(f, x1, x2, x3, e):
    # Coefficient matrix
    A = [[pow(x1, 2), x1, 1], [pow(x2, 2), x2, 1], [pow(x3, 2), x3, 1]]
    b = [f(x1), f(x2), f(x3)]

    print('A = ', A)
    print('b = ', b)

    X = np.linalg.solve(A, b)
    print('ABC')
    print (X)

    a0 = X[0]
    a1 = X[1]
    a2 = X[2]

    x = (-1) * a1 / (2 * a0)
    print('x = ', x)

    if abs(x - x2) < e:
        if f(x) < f(x2):
            y = f(x)
            print(x)
            return (x, y)
        else:
            y = f(x2)
            print(x2)
            return (x2, y)

    arr = [x1, x2, x3, x]
    arr.sort()

    if f(x2) > f(x):
        index = arr.index(x)
        x2 = x
        x1 = arr[index - 1]
        x3 = arr[index + 1]
    else:
        index = arr.index(x2)

        x1 = arr[index - 1]
        x3 = arr[index + 1]

    return search(f, x1, x2, x3, e)


def regre(f, a, b, e):
    x1 = a
    x3 = b
    x2 = (a + b) / 2.0
    p = search(f, x1, x2, x3, e)
    printFunc(f, a, b, p[0], p[1])


a = -1
b = 0
e = 0.003
regre(f, a, b, e)
