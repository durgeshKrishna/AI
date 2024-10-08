import heapq

class Node:
    """Class to represent a node in the search space."""
    def __init__(self, position, heuristic=0):
        self.position = position  # (x, y) coordinates
        self.heuristic = heuristic  # Heuristic value

    def __lt__(self, other):
        return self.heuristic < other.heuristic  # For priority queue sorting

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(start, goal, grid):
    """Greedy Best-First Search algorithm implementation."""
    open_list = []  # Priority queue for nodes to explore
    closed_set = set()  # Set of already explored nodes

    # Add the starting node to the open list
    start_node = Node(start, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)  # Get the node with the lowest heuristic

        # If we reach the goal, return success
        if current_node.position == goal:
            return True

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
                
                # Calculate the heuristic for the neighbor
                neighbor_heuristic = heuristic(neighbor_pos, goal)
                heapq.heappush(open_list, Node(neighbor_pos, neighbor_heuristic))

    return False  # Return False if no path is found

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

    if greedy_best_first_search(start, goal, grid):
        print("Path to the goal found!")
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
