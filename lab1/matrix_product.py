import numpy as np
from helper import generate_vector


def matrix_product(matrix1, matrix2):
    return np.matmul(np.array(matrix1), np.array(matrix2))


if __name__ == "__main__":
    n = 10
    matrix1 = [generate_vector(n) for _ in range(n)]
    matrix2 = [generate_vector(n) for _ in range(n)]
    result = matrix_product(matrix1, matrix2)
    print(result)
