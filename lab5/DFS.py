from lab5.helper import generate_matrix, transfer_matrix_to_adj


def DFS_recursive(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited = DFS_recursive(graph, i, visited)
    return visited


def DFS_iterative(graph, v):
    visited = set()
    traversal = []
    stack = [v]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(graph[vertex][::-1])
    return traversal


m = generate_matrix()
graph = transfer_matrix_to_adj(m)
visited = [False] * len(graph)
# for u in adj_list:
rec = DFS_recursive(graph, 0, visited)
rec_res = []
for i in range(len(rec)):
    if rec[i]:
        rec_res.append(i)

iter_ = DFS_iterative(graph, 0)
print(rec_res)
print(sorted(iter_))
