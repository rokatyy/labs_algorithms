from helper import generate_vector, make_plot, get_parameters, timeit
from numpy import product


@timeit
def get_product(array):
    f = 1
    for _ in array:
        f *= _


@timeit
def np_prod(array):
    product(array)


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(1, max_value+1, step)]
    time = []
    for vector_len in [i for i in range(1, max_value+1, step)]:
        vector = generate_vector(vector_len)
        time.append(get_product(vector))
    make_plot(x, time, 'product')
    time = []
    for vector_len in [i for i in range(1, max_value+1, step)]:
        vector = generate_vector(vector_len)
        time.append(np_prod(vector))
    make_plot(x, time, 'Product_numpy')


