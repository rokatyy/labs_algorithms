from lab1.helper import generate_vector, make_plot, get_parameters, timeit


@timeit
def constant_func():
    f = 1


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(0, max_value, step)]:
        vector = generate_vector(vector_len)
        time.append(constant_func())
    make_plot(x, time, 'constant')
