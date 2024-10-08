from collections import deque

def bfs(graph, start, stop):
    queue = deque([(start, [start], 0)])  # (current node, path, current path cost)
    visited = set()

    while queue:
        node, path, cost = queue.popleft()
        
        if node == stop:
            print(f"Path found: {' -> '.join(path)} with total cost: {cost}")
            return True
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, path_cost in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + path_cost))
                    
    print(f"No path found from {start} to {stop}")
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

bfs(graph, start, stop)
