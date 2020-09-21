import numpy as np
from scipy import optimize

linear = lambda x, a, b: a * x + b
rational = lambda x, a, b: a / (1 + b * x)


def gradient_descent(x, y, theta, alpha, m, numIterations):
    optimize.minimize()


def conjugate_gradient_descent():
    pass


def Levenberg_Marquardt():
    pass


def newtons_method(func, x0, X, Y, eps=0.001):
    fprime = lambda x: optimize.approx_fprime(x, loss, eps)
    return optimize.minimize(loss, x0, args=(X, Y), tol=eps, method='Newton-CG', jac=fprime)


def loss(x0, X, Y, method=linear):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (linear(x_i, x0[0], x0[1]) - y_i) ** 2
    return summary
