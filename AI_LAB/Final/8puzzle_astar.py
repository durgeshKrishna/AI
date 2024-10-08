import heapq

def manhattan_distance(state, goal):
    """
    Calculate the Manhattan distance heuristic for a given state.
    """
    distance = 0
    for num in range(1, 9):  # Tiles 1 through 8
        current_index = state.index(num)
        goal_index = goal.index(num)
        current_row, current_col = divmod(current_index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_successors(state):
    """
    Generate all possible successor states from the current state.
    """
    successors = []
    zero_index = state.index(0)  # Locate the empty tile (0)
    row, col = divmod(zero_index, 3)
    
    # Define possible moves based on the empty tile's position
    moves = []
    if row > 0:
        moves.append(('Up', -3))
    if row < 2:
        moves.append(('Down', 3))
    if col > 0:
        moves.append(('Left', -1))
    if col < 2:
        moves.append(('Right', 1))
    
    for action, delta in moves:
        new_zero_index = zero_index + delta
        # Convert state to list for mutability
        new_state = list(state)
        # Swap the empty tile with the target tile
        new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
        successors.append((tuple(new_state), action))
    
    return successors

def is_solvable(state, goal):
    """
    Determine if the puzzle is solvable by comparing the number of inversions.
    """
    def inversion_count(sequence):
        inv_count = 0
        seq = [num for num in sequence if num != 0]
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if seq[i] > seq[j]:
                    inv_count += 1
        return inv_count
    
    inv_state = inversion_count(state)
    inv_goal = inversion_count(goal)
    return inv_state % 2 == inv_goal % 2

def a_star(start, goal):
    """
    Perform the A* search algorithm to solve the 8-puzzle.
    """
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start, []))
    
    closed_set = set()
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path
        
        if current in closed_set:
            continue
        closed_set.add(current)
        
        for successor, action in get_successors(current):
            if successor in closed_set:
                continue
            new_g = g + 1  # Assuming uniform cost
            new_f = new_g + manhattan_distance(successor, goal)
            heapq.heappush(open_set, (new_f, new_g, successor, path + [action]))
    
    return None  # No solution found

def print_puzzle(state):
    """
    Print the puzzle state in a 3x3 grid format.
    """
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(' '.join(['_' if num == 0 else str(num) for num in row]))
    print()

def main():
    """
    Main function to execute the A* algorithm for the 8-puzzle.
    """
    # Define the initial and goal states
    initial_state = (1, 2, 3,
                     4, 0, 6,
                     7, 5, 8)
    
    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)
    
    print("Initial State:")
    print_puzzle(initial_state)
    
    print("Goal State:")
    print_puzzle(goal_state)
    
    # Check if the puzzle is solvable
    if not is_solvable(initial_state, goal_state):
        print("The given puzzle is not solvable.")
        return
    
    # Perform A* search
    path = a_star(initial_state, goal_state)
    
    if path is None:
        print("No solution exists for the given puzzle.")
    else:
        print(f"Solution found in {len(path)} moves:")
        current_state = initial_state
        print_puzzle(current_state)
        for i, action in enumerate(path):
            print(f"Move {i + 1}: {action}")
            # Generate the next state based on the action
            for successor, act in get_successors(current_state):
                if act == action:
                    current_state = successor
                    break
            print_puzzle(current_state)

if __name__ == "__main__":
    main()
