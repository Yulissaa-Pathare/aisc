graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'F', 'G'],
    'D': ['A', 'E'],
    'E': ['A', 'B', 'C', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['C', 'F']
}

queue = [['A']]
visited = []

while queue:
    path = queue.pop(0)
    node = path[-1]

    if node == 'G':
        print("Path:", path)
        break

    if node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])