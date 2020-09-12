from timer import timeit
from helper import generate_vector, make_plot


@timeit
def get_composition(array):
    f = []
    for i in range(len(array)):
        f.append(array[i - 1] * array[i]) if f else f.append(array[i])


if __name__ == "__main__":
    max_value = 1900
    k = max_value / 10
    step = 1
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(get_composition(vector))
    make_plot(x, time, 'Composition')
