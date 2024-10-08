import heapq

def ucs(graph, start, stop):
    # Priority queue, stores tuples of (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        # Pop the node with the lowest cost
        cost, node, path = heapq.heappop(queue)

        if node == stop:
            print(f"Path found: {' -> '.join(path)} with total cost: {cost}")
            return True

        if node not in visited:
            visited.add(node)
            
            for neighbor, path_cost in graph[node]:
                if neighbor not in visited:
                    # Push the neighbor with updated cost and path
                    heapq.heappush(queue, (cost + path_cost, neighbor, path + [neighbor]))
                    
    print(f"No path found from {start} to {stop}")
    return False

# Graph structure with nodes and edge costs
graph = {
    'A': [('B', 9), ('C', 4)],
    'B': [('A', 9), ('C', 2), ('D', 7)],
    'C': [('A', 4), ('B', 2), ('D', 1), ('E', 6)],
    'D': [('B', 7), ('C', 1), ('E', 4),('F',8)],
    'E': [('C', 6), ('D', 4),('F',2)],
    'F':[('E',2),('D',8)]
}


start = 'A'
stop = 'F'

# Call UCS to find the least-cost path and total cost
ucs(graph, start, stop)
