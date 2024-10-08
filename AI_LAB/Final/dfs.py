def dfs(graph, start, stop, visited=None, path=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    if path is None:
        path = []  # List to store the current path

    visited.add(start)
    path.append(start)

    # Check if the stop node is found
    if start == stop:
        print("Path found:", " -> ".join(path))
        return True

    # Explore the neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, stop, visited, path):  # If path is found, stop recursion
                return True

    # If no path is found, backtrack by removing the current node from the path
    path.pop()
    return False

# Graph definition
graph = {
    'ORADEA': ['ZERIND', 'SIBIU'],
    'ZERIND': ['ORADEA', 'ARAD'],
    'ARAD': [ 'SIBIU','ZERIND', 'TIMISOARA'],
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

# Run DFS to find the path
if not dfs(graph, start, stop):
    print(f"No path found from {start} to {stop}")
