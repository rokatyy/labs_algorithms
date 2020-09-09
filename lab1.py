import random
from timer import timeit
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
from threading import Thread


def generate_vector(n, max_value=10000):
    return [random.randint(0, max_value) for _ in range(n)]


@timeit
def constant_func(array):
    f = [1 for _ in array]


@timeit
def get_sum(array):
    f = []
    for i in range(len(array)):
        f.append(array[i - 1] + array[i]) if f else f.append(array[i])


@timeit
def get_composition(array):
    f = []
    for i in range(len(array)):
        f.append(array[i - 1] * array[i]) if f else f.append(array[i])


@timeit
def naive_polynom(array, x=1):
    f = []
    for i in range(len(array)):
        f.append((array[i] * (x ** (i - 1))))


@timeit
def gorner_polynom(array):
    pass


@timeit
def bubble_sort(array):
    n = len(array)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True


@timeit
def quick_sort(array):
    pass


@timeit
def hybrid(array):
    pass


if __name__ == '__main__':
    constant_time = []
    sum_time = []
    composition_time = []
    gorner_time = []
    bubble_time = []
    quick_time = []
    hybrid_time = []
    x = [i for i in range(100, 1100, 100)]

    for vector_len in x:
        print(f'vector len = {vector_len} ')
        # generate vector
        vector = generate_vector(vector_len)

        # working with vector
        t1 = Thread(target=constant_func, args=[vector])
        t2 = Thread(target=get_sum, args=[vector])
        t3 = Thread(target=get_composition, args=[vector])
        t4 = Thread(target=get_composition, args=[vector])
        t5 = Thread(target=bubble_sort, args=[vector])
        t6 = Thread(target=get_composition, args=[vector])
        t7 = Thread(target=get_composition, args=[vector])

        for thread in [t1, t2, t3, t4, t5, t6, t7]:
            thread.start()

        constant_time.append(t1.join())
        sum_time.append(t2.join())
        composition_time.append(t3.join())

    df = pd.DataFrame({'x': x, 'y': constant_time})
    sb.pointplot(x='x', y='y', data=df)
    plt.show()
