from timer import timeit
from helper import generate_vector, make_plot


@timeit
def naive_polynom(array, x=1):
    f = []
    for i in range(len(array)):
        f.append((array[i] * (x ** (i - 1))))

