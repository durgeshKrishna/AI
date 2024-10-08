# IDA* algorithm for Graph Search

class Graph:
    def __init__(self):
        self.edges = {}  # Adjacency list

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))
    
    def get_neighbors(self, node):
        return self.edges.get(node, [])

# Heuristic Function (Simple example: heuristic as zero)
# In practical scenarios, this should be a function that estimates
# the cost from the current node to the goal node.
def heuristic(node, goal):
    # Example: Dummy heuristic (could be a straight-line distance in certain cases)
    return 0  # Change this if a more complex heuristic is needed

# IDA* Search Algorithm
def ida_star(graph, start, goal):
    def search(path, g, threshold):
        node = path[-1]
        f = g + heuristic(node, goal)

        if f > threshold:
            return f
        if node == goal:
            return "FOUND"
        
        min_threshold = float('inf')
        for (neighbor, cost) in graph.get_neighbors(node):
            if neighbor not in path:  # Avoid revisiting the same node
                path.append(neighbor)
                temp = search(path, g + cost, threshold)
                if temp == "FOUND":
                    return "FOUND"
                if temp < min_threshold:
                    min_threshold = temp
                path.pop()

        return min_threshold

    # Initial threshold set to heuristic of the start node
    threshold = heuristic(start, goal)
    path = [start]

    while True:
        temp = search(path, 0, threshold)
        if temp == "FOUND":
            return path
        if temp == float('inf'):
            return None  # No solution exists
        threshold = temp

# Example Graph Creation and Search Execution
def main():
    # Create a graph
    graph = Graph()

    # Add edges (from_node, to_node, cost)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('C', 'F', 2)
    graph.add_edge('D', 'G', 1)
    graph.add_edge('E', 'G', 1)
    graph.add_edge('F', 'G', 5)

    # Define start and goal nodes
    start = 'A'
    goal = 'G'

    # Perform IDA* search
    solution = ida_star(graph, start, goal)

    if solution:
        print(f"Path found: {solution}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
