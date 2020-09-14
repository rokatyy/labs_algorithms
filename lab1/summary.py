from lab1.helper import generate_vector, make_plot, get_parameters, timeit


@timeit
def get_sum(array):
    res = 0
    for _ in array:
        res += _


@timeit
def builtin_sum(array):
    sum(array)


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(get_sum(vector))
    make_plot(x, time, 'Summary')
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(builtin_sum(vector))
    make_plot(x, time, 'Summary_builtin')
