import numpy as np
from helper import generate_vector, timeit, make_plot, get_parameters


@timeit
def matrix_product(matrix1, matrix2):
    np.matmul(np.array(matrix1), np.array(matrix2))


if __name__ == "__main__":
    max_value, step = get_parameters()
    x = [i for i in range(1, max_value + 1, step)]
    time = []
    for n in [i for i in range(1, max_value + 1, step)]:
        matrix1 = [generate_vector(n) for _ in range(n)]
        matrix2 = [generate_vector(n) for _ in range(n)]
        time.append(matrix_product(matrix1, matrix2))
    make_plot(x, time, 'Matrix product')
