from lab1.timer import timeit
from lab1.helper import generate_vector, make_plot


@timeit
def horner_polynom(vector, x=1):
    p = vector[len(vector)-1]
    for i in range(len(vector) - 2, 0, -1):
        p = p * x + vector[i]


if __name__ == "__main__":
    max_value = 1900
    k = max_value / 10
    step = 1
    x = [i for i in range(0, max_value, step)]
    time = []
    for vector_len in [i for i in range(1, max_value + 1, step)]:
        vector = generate_vector(vector_len)
        time.append(horner_polynom(vector, 1))
    make_plot(x, time, 'Horner polynom', 5)
