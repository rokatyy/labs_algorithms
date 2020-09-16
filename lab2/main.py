import numpy as np
import direct_methods
from math import fabs
import helper

a = 0
b = 1
e = 0.001

if __name__ == "__main__":

    y = (lambda x: x**3)
    minimum, iterations = direct_methods.exhaustive_search(a, b, e, y)
    print(f'Exaustive search for x^3 in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')

    y = (lambda x: fabs(x-0.2))
    minimum, iterations = direct_methods.dichotomy(a, b, e, y)
    print(f'Dichotomy search for |x-0.2| in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')


