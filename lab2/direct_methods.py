from math import ceil


def exhaustive_search(a, b, e, func):
    n = ceil((b - a) / e)
    minimum = min(func([a + k * (b - a) / n for k in range(n)]))
    return minimum, n


def dichotomy():
    pass


def golden_section():
    pass


def gauss():
    pass


def nelder_mead():
    pass
