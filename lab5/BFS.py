from collections import deque


def bfs(graph, start, goal):
    explored = []
    queue = deque([[start]])
    if start == goal:
        return start
    while queue:
        path = queue.popleft()
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
