import heapq

class Node:
    """Class to represent a node in the grid."""
    def __init__(self, position, cost=0):
        self.position = position  # (x, y) coordinates
        self.cost = cost  # Total cost to reach this node

    def __lt__(self, other):
        return self.cost < other.cost  # For priority queue sorting

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    """A* algorithm implementation."""
    open_list = []  # Priority queue for nodes to explore
    closed_set = set()  # Set of already explored nodes

    # Add the starting node to the open list
    start_node = Node(start)
    heapq.heappush(open_list, (0, start_node))  # (priority, node)

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)  # Get the node with the lowest cost
        
        # If we reach the goal, return the total cost
        if current_node.position == goal:
            return current_cost
        
        closed_set.add(current_node.position)  # Mark this node as explored

        # Check the neighbors (up, down, left, right)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direction vectors
        for direction in neighbors:
            neighbor_pos = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
            
            # Check if the neighbor is within bounds and walkable
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):
                
                # Calculate the cost to reach this neighbor
                g_cost = current_cost + 1  # Cost from start to current node
                h_cost = heuristic(neighbor_pos, goal)  # Heuristic cost to goal
                total_cost = g_cost + h_cost  # Total cost

                # Add the neighbor to the open list
                heapq.heappush(open_list, (total_cost, Node(neighbor_pos, total_cost)))

    return None  # Return None if no path is found

def main():
    # Define the grid (0 = walkable, 1 = blocked)
    grid = [
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)  # Starting position (top-left corner)
    goal = (4, 4)   # Goal position (bottom-right corner)

    cost = a_star(start, goal, grid)

    if cost is not None:
        print(f"The cost to reach the goal is: {cost}")
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
