def add_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)

def hill_climbing(start, goals, heuristic_values, graph):
    current = start
    print("Graph:", graph)
    
    while True:
        print(f"Current Node: {current}")
        
        # Check if current node is in any of the goal states
        if current in goals:
            return True
        
        neighbors = graph[current]
        if not neighbors:
            break  # No neighbors to move to, hence terminate
        
        # Find the neighbor with the highest heuristic value
        next_state = max(neighbors, key=heuristic_values.get)
        print(f"Next Node: {next_state} with Heuristic: {heuristic_values[next_state]}")
        
        # If the best neighbor's heuristic is not better, stop
        if heuristic_values[next_state] <= heuristic_values[current]:
            break
        
        current = next_state  # Move to the neighbor with the highest heuristic
    
    return current in goals  # Return if we reached any goal state

# Define the nodes and their heuristic values
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
heuristic_values = {
    'A': 1,  # Lower heuristic for goal nodes
    'B': 2,
    'C': 3,
    'D': 8,
    'E': 7,
    'F': 5,
    'G': 4,
    'H': 6,
    'I': 9
}

# Multiple goal nodes
goal_states = ['A', 'B']  # More than one goal node

# Create a 3-level graph
graph = {node: [] for node in nodes}

# Add edges to create a 3-level graph
add_edge(graph, 'I', 'H')
add_edge(graph, 'H', 'G')
add_edge(graph, 'G', 'F')
add_edge(graph, 'F', 'E')
add_edge(graph, 'E', 'D')
add_edge(graph, 'D', 'C')
add_edge(graph, 'C', 'B')
add_edge(graph, 'B', 'A')

# Starting node
start_state = 'I'

# Perform hill climbing search
reachable = hill_climbing(start_state, goal_states, heuristic_values, graph)
if reachable:
    print(f"One of the goal states {goal_states} is reachable.")
else:
    print(f"None of the goal states {goal_states} are reachable.")
