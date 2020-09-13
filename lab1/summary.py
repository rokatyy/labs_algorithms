from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot, get_parameters


@timeit
def get_sum(array):
    f = []
    for i in range(len(array)):
        f.append(array[i - 1] + array[i]) if f else f.append(array[i])


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(get_sum(vector))
    make_plot(x, time, 'Summary')
