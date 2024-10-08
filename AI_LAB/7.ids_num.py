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

    # If we have reached the depth limit, return False
    if limit <= 0:
        return False

    visited.add(node)

    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            # Recur with reduced depth limit and accumulate the cost
            if dls(graph, neighbor, stop, limit - 1, path + [neighbor], visited, total_cost + cost):
                return True

    return False

def ids(graph, start, stop, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit: {depth}")
        visited = set()  # Clear visited for each depth
        if dls(graph, start, stop, depth):
            # Stop further exploration when the path is found
            return True
        else:
            print(f"Depth {depth} explored, no path found.")
    print(f"No path found from {start} to {stop} within depth limit {max_depth}")
    return False

# Graph structure with nodes and edges
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4), ('D', 7)],
    'C': [('A', 5), ('B', 4), ('D', 2), ('E', 3)],
    'D': [('B', 7), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

start = 'A'
stop = 'B'
max_depth = 4  # Set maximum depth limit

# Call IDS with the start node, goal node, and maximum depth
ids(graph, start, stop, max_depth)
