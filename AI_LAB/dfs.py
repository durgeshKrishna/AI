def dfs(graph, start, stop, visited=None, path=None):
    if visited is None:
        visited = set() 
    if path is None:
        path = []  
    visited.add(start)
    path.append(start)
    if start == stop:
        print("Path found:", " -> ".join(path))
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, stop, visited, path):
                return True
    path.pop()
    return False
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
start = 'ARAD'
stop = 'BUCHAREST'
if not dfs(graph, start, stop):
    print(f"No path found from {start} to {stop}")
