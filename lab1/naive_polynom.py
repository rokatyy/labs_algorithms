from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot, get_parameters


@timeit
def naive_polynom(array, x=1):
    f = []
    for i in range(len(array)):
        f.append((array[i] * (x ** (i - 1))))


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(naive_polynom(vector,5))
    make_plot(x, time, 'Naive polynom',5)
