from collections import deque
def bfs(graph, start, stop):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == stop:
            print("Path found:", " -> ".join(path))
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    print(f"No path found from {start} to {stop}")
    return False
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
start = 'ARAD'
stop = 'BUCHAREST'
bfs(graph, start, stop)
