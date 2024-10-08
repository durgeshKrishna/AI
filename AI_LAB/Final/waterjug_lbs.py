import heapq
import math

# Define Jug Capacities and Target
CAPACITY_A = 4  # Capacity of Jug A in liters
CAPACITY_B = 3  # Capacity of Jug B in liters
TARGET = 2      # Target amount in liters

# Define the initial state
initial_state = (0, 0)  # (Jug A, Jug B)

# Define the Goal Condition
def is_goal(state, target):
    return state[0] == target or state[1] == target

# Heuristic Function: Minimum number of steps needed (simplistic)
def heuristic(state, target):
    x, y = state
    # If either jug has the target, heuristic is 0
    if x == target or y == target:
        return 0
    # Otherwise, heuristic is the minimum difference
    return min(abs(x - target), abs(y - target))

# Function to generate all possible successors from the current state
def get_successors(state):
    successors = []
    x, y = state

    # Fill Jug A
    if x < CAPACITY_A:
        new_state = (CAPACITY_A, y)
        successors.append((new_state, "Fill Jug A"))

    # Fill Jug B
    if y < CAPACITY_B:
        new_state = (x, CAPACITY_B)
        successors.append((new_state, "Fill Jug B"))

    # Empty Jug A
    if x > 0:
        new_state = (0, y)
        successors.append((new_state, "Empty Jug A"))

    # Empty Jug B
    if y > 0:
        new_state = (x, 0)
        successors.append((new_state, "Empty Jug B"))

    # Pour Jug A -> Jug B
    if x > 0 and y < CAPACITY_B:
        pour_amount = min(x, CAPACITY_B - y)
        new_x = x - pour_amount
        new_y = y + pour_amount
        new_state = (new_x, new_y)
        successors.append((new_state, "Pour Jug A to Jug B"))

    # Pour Jug B -> Jug A
    if y > 0 and x < CAPACITY_A:
        pour_amount = min(y, CAPACITY_A - x)
        new_x = x + pour_amount
        new_y = y - pour_amount
        new_state = (new_x, new_y)
        successors.append((new_state, "Pour Jug B to Jug A"))

    return successors

# Function to check if the puzzle is solvable
def is_solvable(capacity_a, capacity_b, target):
    # A solution exists if the target is a multiple of GCD(capacity_a, capacity_b)
    # and the target is less than or equal to the maximum capacity
    return target % math.gcd(capacity_a, capacity_b) == 0 and target <= max(capacity_a, capacity_b)

# Local Beam Search Algorithm
def local_beam_search(start, target, beam_width=2):
    """
    Perform Local Beam Search to solve the Water Jug Problem.
    
    Parameters:
    - start: Tuple representing the starting state (jugA, jugB).
    - target: Integer representing the target amount.
    - beam_width: Integer representing the beam width (number of best candidates to keep).
    
    Returns:
    - A list of actions leading from the start state to the goal state, or None if no solution is found.
    """
    # Initialize the beam with the start state
    # Each element in the beam is a tuple (f_score, state, path)
    beam = [(heuristic(start, target), start, [])]

    # Set to keep track of visited states
    visited = set()

    while beam:
        # Sort the beam based on f_score
        beam = sorted(beam, key=lambda x: x[0])

        # Select the top 'beam_width' states
        current_beam = beam[:beam_width]
        beam = []

        for f_score, state, path in current_beam:
            if is_goal(state, target):
                return path  # Solution found

            if state in visited:
                continue  # Skip already visited states
            visited.add(state)

            # Generate all possible successors
            for successor, action in get_successors(state):
                if successor not in visited:
                    new_path = path + [action]
                    new_f = heuristic(successor, target)
                    beam.append((new_f, successor, new_path))

        if not beam:
            break  # No more states to explore

    return None  # No solution found

# Function to print the sequence of actions and states
def print_solution(path):
    """
    Print the sequence of actions and corresponding states.
    
    Parameters:
    - path: List of actions leading to the goal.
    """
    current_state = initial_state
    print(f"Initial State: Jug A = {current_state[0]} liters, Jug B = {current_state[1]} liters\n")

    for i, action in enumerate(path, 1):
        print(f"Step {i}: {action}")
        # Generate the next state based on the action
        for successor, act in get_successors(current_state):
            if act == action:
                current_state = successor
                break
        print(f"Resulting State: Jug A = {current_state[0]} liters, Jug B = {current_state[1]} liters\n")

    print(f"Total Steps: {len(path)}")

# Main Function
def main():
    # Check if the puzzle is solvable
    if not is_solvable(CAPACITY_A, CAPACITY_B, TARGET):
        print("No solution exists for the given puzzle.")
        return

    # Perform Local Beam Search
    beam_width = 2  # Adjust beam width as needed
    solution_path = local_beam_search(initial_state, TARGET, beam_width)

    # Display the result
    if solution_path:
        print("Solution Found!\n")
        print_solution(solution_path)
    else:
        print("No solution found within the given beam width.")

if __name__ == "__main__":
    main()
