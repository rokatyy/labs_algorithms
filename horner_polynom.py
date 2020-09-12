from timer import timeit
from helper import generate_vector, make_plot


@timeit
def horner_polynom(poly, x=1):
    f = [poly[0]]
    for i in range(1, len(poly)):
        f.append(poly[i - 1] * x + poly[i])