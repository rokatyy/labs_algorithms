from lab5.helper import generate_matrix, transfer_matrix_to_adj


def BFS(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return start
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)

    print("Not connected")
    return


m = generate_matrix()
graph = transfer_matrix_to_adj(m)
print(graph)
x=BFS(graph, 0, 1)
print(x)
