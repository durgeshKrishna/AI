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
    Each successor is a tuple (new_state, action_description).
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

def is_goal(state, goal):
    """
    Check if the current state is the goal state.
    """
    return state == goal

def beam_search_8_puzzle(initial_state, goal_state, beam_width=3):
    """
    Perform Beam Search to solve the 8-Puzzle problem.

    Parameters:
    - initial_state: Tuple representing the starting configuration.
    - goal_state: Tuple representing the goal configuration.
    - beam_width: Number of best nodes to keep at each level.

    Returns:
    - A list of states representing the path from start to goal, or None if no path is found.
    """
    def heuristic(state):
        return manhattan_distance(state, goal_state)
    
    # Initialize the beam with the start state
    beam = [(heuristic(initial_state), initial_state, [initial_state])]
    
    while beam:
        # Check for goal in current beam
        for f, state, path in beam:
            if is_goal(state, goal_state):
                return path
        
        # Generate all successors from the current beam
        all_successors = []
        for f, state, path in beam:
            for successor, action in get_successors(state):
                if successor not in path:  # Avoid cycles
                    new_path = path + [successor]
                    new_f = heuristic(successor)
                    all_successors.append((new_f, successor, new_path))
        
        if not all_successors:
            break  # No more nodes to expand
        
        # Select the best 'beam_width' successors based on heuristic
        # Lower heuristic values are better
        beam = heapq.nsmallest(beam_width, all_successors, key=lambda x: x[0])
    
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
    
    # Perform Beam Search
    beam_width = 3  # You can adjust the beam width
    path = beam_search_8_puzzle(initial_state, goal_state, beam_width)
    
    if path:
        print(f"Solution found in {len(path)-1} moves:")
        for i, state in enumerate(path):
            print(f"Step {i}:")
            print_puzzle(state)
    else:
        print("No solution found with the given beam width.")

if __name__ == "__main__":
    main()
