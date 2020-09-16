import numpy as np
import direct_methods
import math
import helper

a = 0.01
b = 1
e = 0.001


def one_dimensional(y, description, a, b, e):
    minimum, iterations = direct_methods.exhaustive_search(a, b, e, y)
    print(
        f'Exaustive search for {description} in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')

    minimum, iterations = direct_methods.dichotomy(a, b, e, y)
    print(
        f'Dichotomy search for {description} in [{a},{b}] with e={e} found minimal value in {minimum}, iteration count: {iterations}.')

    minimum, iterations = direct_methods.golden_section(a, b, e, y)
    print(
        f'Golden section search for {description} in [{a},{b}] with e={e} found minimal value in {minimum}, iteration count: {iterations}.\n')


if __name__ == "__main__":
    funcs = [((lambda x: x ** 3), 'x^3'), ((lambda x: abs(x - 0.2)), '|x - 0.2|'), (lambda x: x* math.sin(1/x),'x * sin(1/x)')]

    for y in funcs:
        one_dimensional(y[0], y[1], a, b, e)
