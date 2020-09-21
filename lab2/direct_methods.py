from math import ceil, fabs
import numpy as np

def exhaustive_search(a, b, e, func):
    n = ceil((b - a) / e)
    minimum = None
    for k in range(n):
        x = a + k * (b - a) / n
        if not minimum or func(x) < func(minimum):
            minimum = x
    return minimum, n


def dichotomy(a, b, e, func):
    iterations = 0
    s = e / 2
    while fabs(a - b) >= e:
        x1, x2 = (a + b - s) / 2, (a + b + s) / 2
        if func(x1) <= func(x2):
            a, b = a, x2
        else:
            a, b = x1, b
        iterations += 1
    return (a, b), iterations


def golden_section(a, b, e, func):
    iterations = 0
    gs = (3 - np.sqrt(5)) / 2
    x1, x2 = a + gs * (b - a), b - gs * (b - a)
    y1, y2 = func(x1), func(x2)
    while fabs(a - b) >= e:
        if y1 <= y2:
            b, x2, y2 = x2, x1, y1
            x1 = a + gs * (b - a)
            y1 = func(x1)
        else:
            a, x1, y1 = x1, x2, y2
            x2 = b - gs * (b - a)

            y2 = func(x2)
        iterations += 1

    return (a, b), iterations


linear = lambda x, a, b: a * x + b
rational = lambda x, a, b: a / (1 + b * x)


def exhaustive_search_multi(func, X, Y, k=100, e=0.001):
    a_min, a_max = -2, 2
    b_min, b_max = -2, 2
    n_a = ceil((a_max - a_min) / e)
    n_b = ceil((b_max - b_min) / e)
    min_pair = None
    min_sum = None
    for a in [a_min + e * i for i in range(n_a)]:
        for b in [b_min + e * i for i in range(n_b)]:
            value = D(func, a, b, k, X, Y)
            if not min_sum or value < min_sum:
                min_sum = value
                min_pair = (a, b)
    return min_pair


def loss(x0, X, Y, method):
    summary = 0
    for x_i, y_i in zip(X, Y):
        summary += (method(x_i, x0[0], x0[1]) - y_i) ** 2
    return summary


def D(func, a, b, k, X, Y):
    try:
        return sum([(func(X[i], a, b) - Y[i]) ** 2 for i in range(k)])
    # а это костыль
    except:
        return 10**2


