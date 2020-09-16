from math import ceil, fabs
import numpy as np


def exhaustive_search(a, b, e, func):
    n = ceil((b - a) / e)
    minimum = min([func(a + k * (b - a)) for k in range(n)])
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


def gauss():
    pass


def nelder_mead():
    pass
