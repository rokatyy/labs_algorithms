import numpy as np
import networkx as nx


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
                    weight = np.random.randint(1, 100)
                    matrix[j][i] = matrix[i][j] = weight
                    cur_edges += 1
    return matrix


def generate_grid(n=10, obs=30):
    expected_probability = int(200 * obs / (2 * n * (n - 1)))
    cur_obs = 0
    G = nx.grid_graph(dim=[10, 10])
    matrix = np.ones((n, n))
    while cur_obs < obs:
        if cur_obs == obs:
            break
        for i in range(n):
            for j in range(n):
                value = np.random.randint(0, 100) <= expected_probability
                if value and cur_obs < obs and matrix[i][j]:
                    G.remove_node((i, j))
                    matrix[i][j] = 0
                    cur_obs += 1
    return G
