from lab1.helper import generate_vector, make_plot, get_parameters, timeit


@timeit
def naive_polynom(array, x=1):
    f = array[0]
    for k in range(1, len(array)):
        f += array[k] * (x ** k)


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(1, max_value+1, step)]
    time = []
    for vector_len in [i for i in range(1, max_value+1, step)]:
        vector = generate_vector(vector_len)
        time.append(naive_polynom(vector, 1.5))
    make_plot(x, time, 'Naive polynom', 2)
