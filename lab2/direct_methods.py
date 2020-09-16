from math import ceil, fabs


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


def golden_section():
    pass


def gauss():
    pass


def nelder_mead():
    pass
