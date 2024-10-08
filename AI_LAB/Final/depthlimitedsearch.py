class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to hold the graph

    def add_edge(self, u, v):
        """Adds an edge from node u to node v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, node, goal, depth):
        """Performs Depth-Limited Search."""
        if depth == 0:
            return node == goal  # If we are at the depth limit, check if it is the goal
        if depth > 0:
            if node in self.graph:  # Check if the node has neighbors
                for neighbor in self.graph[node]:
                    if self.dls(neighbor, goal, depth - 1):
                        return True
        return False

    def depth_limited_search(self, start, goal, depth_limit):
        """Starts the Depth-Limited Search from start to goal."""
        return self.dls(start, goal, depth_limit)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')

    start_node = 'A'
    goal_node = 'H'
    depth_limit = 3

    if g.depth_limited_search(start_node, goal_node, depth_limit):
        print(f"Goal '{goal_node}' found within depth limit.")
    else:
        print(f"Goal '{goal_node}' not found within depth limit.")
