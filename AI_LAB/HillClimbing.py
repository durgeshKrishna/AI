def add_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)
def hill_climbing(start, goal, heuristic_values, graph):
    current = start
    print(graph)
    while True:
        if current == goal:
            return True
        neighbors = graph[current]
        if not neighbors:
            break
        next_state = max(neighbors, key=heuristic_values.get)
        if heuristic_values[next_state] <= heuristic_values[current]:
            break
        current = next_state
    return current == goal

nodes = ['A', 'B', 'C', 'D', 'E']
heuristic_values = {
    'E': 2,
    'D': 4,
    'C': 6,
    'B': 7,
    'A': 8
}
goal_state = 'A'
graph = {node: [] for node in nodes}
print(graph)
add_edge(graph, 'A', 'B')
add_edge(graph, 'B', 'C')
add_edge(graph, 'C', 'D')
add_edge(graph, 'D', 'E')
reachable = hill_climbing('E', goal_state, heuristic_values, graph)
if reachable:
    print(f"The goal state '{goal_state}' is reachable.")
else:
    print(f"The goal state '{goal_state}' is not reachable.")




