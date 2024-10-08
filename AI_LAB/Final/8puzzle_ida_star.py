import sys

# Define the goal state for the 8-puzzle
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)  # 0 represents the empty tile

# Possible moves: Up, Down, Left, Right
MOVES = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}

def manhattan_distance(state):
    """
    Calculate the Manhattan distance heuristic for a given state.
    """
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue  # Skip the empty tile
        # Calculate the target position
        target_index = GOAL_STATE.index(tile)
        # Calculate row and column for current and target positions
        current_row, current_col = divmod(index, 3)
        target_row, target_col = divmod(target_index, 3)
        # Add the distance
        distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

def get_successors(state):
    """
    Generate all possible successor states from the current state.
    """
    successors = []
    zero_index = state.index(0)  # Locate the empty tile
    zero_row, zero_col = divmod(zero_index, 3)

    # Define possible movements based on the empty tile's position
    possible_moves = []
    if zero_row > 0:
        possible_moves.append('Up')
    if zero_row < 2:
        possible_moves.append('Down')
    if zero_col > 0:
        possible_moves.append('Left')
    if zero_col < 2:
        possible_moves.append('Right')

    # Generate new states based on possible moves
    for move in possible_moves:
        delta = MOVES[move]
        new_zero_index = zero_index + delta

        # Create a new state as a list for mutability
        new_state = list(state)
        # Swap the empty tile with the target tile
        new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
        # Convert back to tuple and add to successors
        successors.append(tuple(new_state))

    return successors

def ida_star(start_state):
    """
    Perform the IDA* search algorithm to solve the 8-puzzle.
    """
    threshold = manhattan_distance(start_state)  # Initial threshold
    path = [start_state]  # Current path

    while True:
        temp = search(path, 0, threshold)
        if temp == "FOUND":
            return path
        if temp == float('inf'):
            return None  # No solution exists
        threshold = temp  # Update threshold

def search(path, g, threshold):
    """
    Recursive search function for IDA*.
    """
    current_state = path[-1]
    f = g + manhattan_distance(current_state)

    if f > threshold:
        return f
    if current_state == GOAL_STATE:
        return "FOUND"

    min_threshold = float('inf')

    # Generate all possible successors
    successors = get_successors(current_state)

    for state in successors:
        if state not in path:  # Avoid cycles
            path.append(state)
            temp = search(path, g + 1, threshold)
            if temp == "FOUND":
                return "FOUND"
            if temp < min_threshold:
                min_threshold = temp
            path.pop()  # Backtrack

    return min_threshold

def print_solution(path):
    """
    Print the sequence of moves from the start to the goal state.
    """
    move_count = 0
    for state in path:
        move_count += 1
        print(f"Step {move_count}:")
        display(state)
        print()

def display(state):
    """
    Display the 8-puzzle state in a 3x3 grid.
    """
    for i in range(0, 9, 3):
        row = ""
        for j in range(3):
            tile = state[i + j]
            if tile == 0:
                row += " _ "
            else:
                row += f" {tile} "
        print(row)
    print("-" * 9)

def main():
    """
    Main function to execute the IDA* algorithm.
    """
    # Example start state (can be modified)
    # 1 2 3
    # 4 0 6
    # 7 5 8
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    print("Initial State:")
    display(start_state)
    print("Solving...\n")

    solution = ida_star(start_state)

    if solution:
        print("Solution Found!\n")
        print_solution(solution)
    else:
        print("No solution exists for the given puzzle.")

if __name__ == "__main__":
    main()
