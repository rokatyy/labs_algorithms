import numpy as np
import direct_methods
import helper

a = 0
b = 1
e = 0.001


def one_dimensional(y, description, a, b, e):
    minimum, iterations = direct_methods.exhaustive_search(a, b, e, y)
    print(
        f'Exaustive search for {description} in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')

    minimum, iterations = direct_methods.dichotomy(a, b, e, y)
    print(
        f'Dichotomy search for {description} in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')

    minimum, iterations = direct_methods.golden_section(a, b, e, y)
    print(
        f'Golden section search for {description} in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')


if __name__ == "__main__":
    funcs = [((lambda x: abs(x - 0.2)), '|x-0.2|')]

    for y in funcs:
        one_dimensional(y[0], y[1], a, b, e)
