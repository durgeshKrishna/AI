def dls(graph, node, stop, limit, path=None, visited=None, total_cost=0):
    if visited is None:
        visited = set()
    if path is None:
        path = [node]
    
    # If we have reached the goal node, return the path and the total cost
    if node == stop:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Total path cost: {total_cost}")
        return True
    
    # If we have reached the depth limit, return False (stop further exploration)
    if limit <= 0:
        return False

    visited.add(node)
    
    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            # Recur with depth reduced by 1 and update the total cost
            if dls(graph, neighbor, stop, limit - 1, path + [neighbor], visited, total_cost + cost):
                return True

    return False

# Graph structure with nodes and edges
graph = {
    'A': [('B', 9), ('C', 4)],
    'B': [('A', 9), ('C', 2), ('D', 7)],
    'C': [('A', 4), ('B', 2), ('D', 1), ('E', 6)],
    'D': [('B', 7), ('C', 1), ('E', 4), ('F', 8)],
    'E': [('C', 6), ('D', 4), ('F', 2)],
    'F': [('E', 2), ('D', 8)]
}

start = 'A'
stop = 'E'
limit = 3  # Set depth limit

# Call DLS with the start node, goal node, depth limit, and total cost
if not dls(graph, start, stop, limit):
    print(f"No path found from {start} to {stop} within depth limit {limit}")
