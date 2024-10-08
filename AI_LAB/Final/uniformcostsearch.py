import heapq

class Graph:
    def __init__(self):
        self.edges = {}  # Dictionary to hold the graph edges

    def add_edge(self, u, v, cost):
        """Adds an edge from node u to node v with a given cost."""
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, cost))

    def uniform_cost_search(self, start, goal):
        """Performs Uniform Cost Search to find the least-cost path from start to goal."""
        # Priority queue to hold the nodes to be explored
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))  # (cost, node)
        
        # Dictionary to hold the minimum cost to reach each node
        cost_to_node = {start: 0}
        # Dictionary to hold the path to the goal
        came_from = {start: None}

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                return self.reconstruct_path(came_from, start, goal)

            if current_node in self.edges:  # Check if the node has neighbors
                for neighbor, cost in self.edges[current_node]:
                    new_cost = current_cost + cost

                    # If the neighbor hasn't been visited or we've found a cheaper path
                    if neighbor not in cost_to_node or new_cost < cost_to_node[neighbor]:
                        cost_to_node[neighbor] = new_cost
                        came_from[neighbor] = current_node
                        heapq.heappush(priority_queue, (new_cost, neighbor))

        return None  # No path found

    def reconstruct_path(self, came_from, start, goal):
        """Reconstructs the path from start to goal."""
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 2)

    start_node = 'A'
    goal_node = 'E'

    path = g.uniform_cost_search(start_node, goal_node)
    if path:
        print(f"Least-cost path from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
    else:
        print(f"No path found from '{start_node}' to '{goal_node}'.")
