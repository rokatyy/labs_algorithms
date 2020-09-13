from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot


@timeit
def constant_func():
    f = 1


if __name__ == "__main__":
    max_value = 1900
    k = max_value / 10
    step = 1
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(constant_func())
    make_plot(x, time, 'constant')
