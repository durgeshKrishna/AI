import heapq

class Graph:
    """
    A simple graph represented as an adjacency list.
    Each node maps to a list of tuples (neighbor, cost).
    """
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, cost=1):
        """
        Adds a directed edge from 'from_node' to 'to_node' with the given 'cost'.
        """
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def get_neighbors(self, node):
        """
        Returns the neighbors of the given 'node'.
        """
        return self.edges.get(node, [])

def heuristic(node, goal, heuristic_values):
    """
    Heuristic function estimating the cost from 'node' to 'goal'.
    'heuristic_values' is a dictionary containing precomputed heuristic values for each node.
    """
    return heuristic_values.get(node, float('inf'))

def beam_search(graph, start, goal, beam_width, heuristic_values):
    """
    Performs Beam Search on the given 'graph' from 'start' to 'goal' using the specified 'beam_width'.

    Parameters:
    - graph: An instance of the Graph class.
    - start: The starting node.
    - goal: The goal node.
    - beam_width: The number of best nodes to keep at each level.
    - heuristic_values: A dictionary with heuristic estimates for each node.

    Returns:
    - A list representing the path from 'start' to 'goal' if found.
    - None if no path is found within the beam constraints.
    """
    # Initialize the beam with the start node
    # Each element in the beam is a tuple (f_score, node, path)
    initial_h = heuristic(start, goal, heuristic_values)
    beam = [(initial_h, start, [start])]

    while beam:
        # Check if any node in the current beam is the goal
        for f_score, node, path in beam:
            if node == goal:
                return path

        # Generate all possible successors from the current beam
        all_successors = []
        for f_score, node, path in beam:
            for neighbor, cost in graph.get_neighbors(node):
                if neighbor not in path:  # Avoid cycles
                    new_path = path + [neighbor]
                    new_g = len(new_path) - 1  # Assuming uniform cost of 1
                    new_f = new_g + heuristic(neighbor, goal, heuristic_values)
                    all_successors.append((new_f, neighbor, new_path))

        if not all_successors:
            break  # No more nodes to explore

        # Select the best 'beam_width' successors based on f_score
        # Lower f_score is better
        # Use heapq.nsmallest for efficient selection
        beam = heapq.nsmallest(beam_width, all_successors, key=lambda x: x[0])

    # If the goal was not found within the beam constraints
    return None

def main():
    # Create a graph instance
    graph = Graph()

    # Define edges of the graph
    # Example Graph:
    # A --1--> B --1--> D --1--> G
    # A --3--> C --2--> F --5--> G
    # B --4--> E --1--> G
    # C --5--> G

    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('C', 'F', 2)
    graph.add_edge('C', 'G', 5)
    graph.add_edge('D', 'G', 1)
    graph.add_edge('E', 'G', 1)
    graph.add_edge('F', 'G', 5)

    # Define heuristic values for each node (precomputed)
    # For demonstration, we'll use straight-line estimates to the goal 'G'
    heuristic_values = {
        'A': 3,
        'B': 2,
        'C': 4,
        'D': 1,
        'E': 1,
        'F': 2,
        'G': 0
    }

    # Define start and goal nodes
    start_node = 'A'
    goal_node = 'G'

    # Define beam width
    beam_width = 2  # Adjust as needed

    # Perform Beam Search
    path = beam_search(graph, start_node, goal_node, beam_width, heuristic_values)

    # Display the result
    if path:
        print(f"Path found with beam width {beam_width}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node} with beam width {beam_width}.")

if __name__ == "__main__":
    main()
