graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 2, 'G': 3},
    'D': {'H': 3},
    'E': {'H': 4},
    'F': {'H': 3},
    'G': {'H': 2},
    'H': {}
}

h = {
    'A': 5, 'B': 4, 'C': 3, 'D': 3,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}

open_list = [('A', 0)]
parent = {'A': None}
g = {'A': 0}

while open_list:
    open_list.sort(key=lambda x: x[1] + h[x[0]])
    node, f = open_list.pop(0)

    if node == 'H':
        break

    for neighbor in graph[node]:
        cost = g[node] + graph[node][neighbor]

        if neighbor not in g or cost < g[neighbor]:
            g[neighbor] = cost
            parent[neighbor] = node
            open_list.append((neighbor, cost))

path = []
node = 'H'

while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()

print("Path:", path)
print("Total Cost:", g['H'])