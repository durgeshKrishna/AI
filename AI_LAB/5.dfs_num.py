def dfs(graph, start, stop, visited=None, path=None, total_cost=0):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)
    
    if start == stop:
        print(f"Path found: {' -> '.join(path)} with total cost: {total_cost}")
        return True
    
    for neighbor, cost in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, stop, visited, path + [neighbor], total_cost + cost):
                return True

    return False

# Graph structure with nodes and edge costs
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4), ('D', 7)],
    'C': [('A', 5), ('B', 4), ('D', 2), ('E', 3)],
    'D': [('B', 7), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

start = 'A'
stop = 'E'

# Call DFS to find the path and total cost
if not dfs(graph, start, stop):
    print(f"No path found from {start} to {stop}")
