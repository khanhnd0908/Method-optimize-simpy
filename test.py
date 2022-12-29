import numpy as np
from sympy import *
import math
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

# Initialization
x1, x2, t = symbols('x1, x2, t')


def func():
    # Function customization
    return 3 * x1 * x1 + 4 * x1 * x2 + x2 * x2 - 8 * x1 - 12 * x2


def grad(data):
    f = func()
    grad_vec = [diff(f, x1), diff(f, x2)]  # Find partial derivatives, gradientvectors
    grad = []
    for item in grad_vec:
        grad.append(item.subs(x1, data[0]).subs(x2, data[1]))
    return grad


def grad_len(grad):
    vec_len = math.sqrt(pow(grad[0], 2) + pow(grad[1], 2))
    return vec_len


def station(f):
    # Find the stationary point of min(t),in order to get best step size
    t_diff = diff(f)
    t_min = solve(t_diff)
    return t_min


def main(X0, theta):
    f = func()
    grad_vec = grad(X0)
    grad_length = grad_len(grad_vec)  # The modulus length of the gradient vector
    k = 0
    data_x = [0]
    data_y = [0]
    while grad_length > theta:  # Termination conditions of the iteration
        k += 1
        p = -np.array(grad_vec)
        # Iteration
        X = np.array(X0) + t * p
        t_func = f.subs(x1, X[0]).subs(x2, X[1])
        t_min = station(t_func)
        X0 = np.array(X0) + t_min * p
        grad_vec = grad(X0)
        grad_length = grad_len(grad_vec)
        extr = 3 * X0[0] * X0[0] + 4 * X0[0] * X0[1] + X0[1] * X0[1] - 8 * X0[0] - 12 * X0[1]
        print('grad_length', grad_length)
        print('Coordinates', float(X0[0]), float(X0[1]))
        print('Extr', float(extr))
        data_x.append(X0[0])
        data_y.append(X0[1])
    print(k)


if __name__ == '__main__':
    # Given an initial iteration point and a threshold value
    main([0, 0], 0.1)
