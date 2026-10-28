graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

visited = []

def dfs(node):
    visited.append(node)

    if node == 'G':
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor):
                return True

    return False

dfs('A')
print("Path:", visited)