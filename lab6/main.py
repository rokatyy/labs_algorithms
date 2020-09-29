import networkx as nx
from lab6.helper import generate_matrix, generate_grid
from random import randint
from time import time
from timeit import timeit

G = nx.from_numpy_matrix(generate_matrix(400, 2000))
src = randint(0, 100)
d_time = 0
fb_time = 0
for _ in range(1):
    dijkstra_time = timeit(lambda: nx.shortest_path(G, src, method='dijkstra'), number=10)
    d_time += dijkstra_time
    bf_time = timeit(lambda: nx.shortest_path(G, src, method='bellman-ford'), number=10)
    fb_time += bf_time
print(f'dijkstra_time: {dijkstra_time}, bf_time:{bf_time}')
print(f'dijkstra_time: {d_time/30}, bf_time:{fb_time/30}')

print("Part2. A*")

for _ in range(10):

    grid = generate_grid()
    src_i = randint(0, 9)
    trg_i = randint(0, 9)
    trg_j = randint(0, 9)
    src_j = randint(0, 9)
    while not ((src_i, src_j) in grid and (trg_i, trg_j) in grid):
        src_i = randint(0, 9)
        trg_i = randint(0, 9)
        trg_j = randint(0, 9)
        src_j = randint(0, 9)
    try:
        astar_time = timeit(lambda: nx.astar_path(grid, (src_i, src_j), (trg_i, trg_j)), number=5)*1000
        print(astar_time)
    except nx.exception.NetworkXNoPath:
        print('No path.')

