from collections import deque

def bfs(graph, start, stop):
    # Initialize the queue with the starting node and its path
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        # Dequeue the front node and the path leading to it
        node, path = queue.popleft()

        # If the current node is the destination, return the path
        if node == stop:
            print("Path found:", " -> ".join(path))
            return True

        # Mark the node as visited
        if node not in visited:
            visited.add(node)

            # Add all unvisited neighbors to the queue with their respective paths
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    # If no path is found
    print(f"No path found from {start} to {stop}")
    return False

# Graph definition
graph = {
    'ORADEA': ['ZERIND', 'SIBIU'],
    'ZERIND': ['ORADEA', 'ARAD'],
    'ARAD': ['ZERIND', 'SIBIU', 'TIMISOARA'],
    'SIBIU': ['ORADEA', 'ARAD', 'FAGARAS', 'RIMNICU_VILCEA'],
    'TIMISOARA': ['ARAD', 'LUGOJ'],
    'LUGOJ': ['TIMISOARA', 'MEHADIA'],
    'MEHADIA': ['LUGOJ', 'DROBETA'],
    'DROBETA': ['MEHADIA', 'CRAIOVA'],
    'CRAIOVA': ['DROBETA', 'PITESTI', 'RIMNICU_VILCEA'],
    'PITESTI': ['CRAIOVA', 'BUCHAREST'],
    'BUCHAREST': ['PITESTI', 'GIURGIU', 'URZICENI', 'FAGARAS'],
    'GIURGIU': ['BUCHAREST'],
    'URZICENI': ['BUCHAREST', 'HIRSOVA', 'VASLUI'],
    'HIRSOVA': ['URZICENI', 'EFORIE'],
    'EFORIE': ['HIRSOVA'],
    'VASLUI': ['URZICENI', 'IASI'],
    'IASI': ['VASLUI', 'NEAMT'],
    'NEAMT': ['IASI'],
    'FAGARAS': ['BUCHAREST', 'SIBIU'],
    'RIMNICU_VILCEA': ['CRAIOVA', 'SIBIU']
}

# Starting and stopping nodes
start = 'ARAD'
stop = 'BUCHAREST'

# Run BFS to find the path
bfs(graph, start, stop)
