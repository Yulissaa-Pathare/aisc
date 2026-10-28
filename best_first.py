graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

h = {
    'A': 6, 'B': 4, 'C': 3, 'D': 2,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}

open_list = ['A']
visited = []
parent = {'A': None}

while open_list:
    node = min(open_list, key=lambda n: h[n])
    open_list.remove(node)
    visited.append(node)

    if node == 'H':
        break

    for neighbor in graph[node]:
        if neighbor not in visited and neighbor not in open_list:
            open_list.append(neighbor)
            parent[neighbor] = node

path = []
node = 'H'

while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()

print("Path:", path)
print("Visited:", visited)