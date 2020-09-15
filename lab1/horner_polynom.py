from lab1.helper import generate_vector, make_plot, get_parameters, timeit


@timeit
def horner_polynom(vector, x=1):
    p = vector[-1]
    for i in range(-2, -len(vector) - 1, -1):
        p = p * x + vector[i]


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(1, max_value + 1, step)]:
        vector = generate_vector(vector_len)
        time.append(horner_polynom(vector, 1.5))
    make_plot(x, time, 'Horner polynom', 2)
