import numpy as np
import direct_methods
import helper

a = 0
b = 1
e = 0.001

if __name__ == "__main__":
    y = (lambda x: [i ** 3 for i in x])
    minimum, iterations = direct_methods.exhaustive_search(a, b, e, y)
    print(f'Exaustive search in [{a},{b}] with e={e} found minimal value={minimum}, iteration count: {iterations}.')
