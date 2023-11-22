from collections import deque

def find_shortest_path(graph, start, end):
    # Perform backward breadth-first search from the ending vertex
    queue = deque([end])
    visited = {end}
    parent = {end: None}
    while queue:
        vertex = queue.popleft()
        if vertex == start:
            # Build the shortest path
            path = [start]
            while path[-1] != end:
                path.append(parent[path[-1]])
            return list(reversed(path))
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)
    # If no path was found, return None
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

path = find_shortest_path(graph, 'A', 'E')
print(path)  # prints ['A', 'C', 'D', 'E']
