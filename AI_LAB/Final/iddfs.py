class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to hold the graph

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, node, goal, depth):
        if depth == 0 and node == goal:
            return True
        if depth > 0:
            if node in self.graph:  # Check if the node has neighbors
                for neighbor in self.graph[node]:
                    if self.dfs(neighbor, goal, depth - 1):
                        return True
        return False

    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            print(f"Depth Limit: {depth}")
            if self.dfs(start, goal, depth):
                return True
        return False

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
    max_depth = 4

    if g.iddfs(start_node, goal_node, max_depth):
        print(f"Goal '{goal_node}' found!")
    else:
        print(f"Goal '{goal_node}' not found within depth limit.")
