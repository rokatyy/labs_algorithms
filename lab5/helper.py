import numpy as np


def generate_matrix(n=100, edges=200):
    expected_probability = int(200 * edges / (n * (n - 1)))
    cur_edges = 0
    matrix = np.zeros((n, n))
    while cur_edges < edges:
        if cur_edges == edges:
            break
        for i in range(n - 1):
            for j in range(i + 1, n):
                value = np.random.randint(0, 100) <= expected_probability
                if value and cur_edges < edges and not matrix[i][j]:
                    matrix[j][i] = matrix[i][j] = int(value)
                    cur_edges += 1
    return matrix


def transfer_matrix_to_adj(matrix):
    n = len(matrix)
    adj_list = dict((key, []) for key in range(n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if matrix[i][j]:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list

