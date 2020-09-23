from lab5.helper import generate_matrix, transfer_matrix_to_adj


queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


m = generate_matrix()
graph = transfer_matrix_to_adj(m)
bfs([], graph,0)