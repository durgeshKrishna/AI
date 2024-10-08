# Water Jug Problem Solver using IDA* Algorithm

import math
from collections import deque

# Define Jug Capacities and Target
CAPACITY_A = 4  # Capacity of Jug A in liters
CAPACITY_B = 3  # Capacity of Jug B in liters
TARGET = 2      # Target amount in liters

# Define the initial state and goal condition
initial_state = (0, 0)  # Both jugs are empty initially

# Define possible actions
def get_successors(state):
    successors = []
    x, y = state

    # Fill Jug A
    successors.append(((CAPACITY_A, y), "Fill Jug A"))

    # Fill Jug B
    successors.append(((x, CAPACITY_B), "Fill Jug B"))

    # Empty Jug A
    successors.append(((0, y), "Empty Jug A"))

    # Empty Jug B
    successors.append(((x, 0), "Empty Jug B"))

    # Pour Jug A -> Jug B
    pour_to_B = min(x, CAPACITY_B - y)
    new_x = x - pour_to_B
    new_y = y + pour_to_B
    successors.append(((new_x, new_y), "Pour Jug A to Jug B"))

    # Pour Jug B -> Jug A
    pour_to_A = min(y, CAPACITY_A - x)
    new_x = x + pour_to_A
    new_y = y - pour_to_A
    successors.append(((new_x, new_y), "Pour Jug B to Jug A"))

    return successors

# Enhanced Heuristic Function
def heuristic(state, target):
    x, y = state
    # If either jug already has the target, heuristic is 0
    if x == target or y == target:
        return 0
    # Otherwise, the heuristic is 1 (indicating at least one more move is needed)
    return 1

# IDA* Search Function
def ida_star(start, goal):
    threshold = heuristic(start, goal)
    path = [start]
    actions = ["Start"]

    while True:
        temp = search(path, actions, 0, threshold, goal)
        if temp == "FOUND":
            return actions
        if temp == float('inf'):
            return None  # No solution exists
        threshold = temp

# Recursive Search Function
def search(path, actions, g, threshold, goal):
    current = path[-1]
    f = g + heuristic(current, goal)

    if f > threshold:
        return f
    if current[0] == goal or current[1] == goal:
        return "FOUND"

    min_threshold = float('inf')

    # Generate all possible successors
    successors = get_successors(current)

    for (state, action) in successors:
        if state not in path:  # Avoid cycles
            path.append(state)
            actions.append(action)
            temp = search(path, actions, g + 1, threshold, goal)
            if temp == "FOUND":
                return "FOUND"
            if temp < min_threshold:
                min_threshold = temp
            path.pop()
            actions.pop()

    return min_threshold

# Function to check if the puzzle is solvable
def is_solvable(capacity_A, capacity_B, target):
    return target % math.gcd(capacity_A, capacity_B) == 0 and target <= max(capacity_A, capacity_B)

# Function to display the sequence of actions
def print_solution(actions):
    for step, action in enumerate(actions):
        print(f"Step {step}: {action}")

# Main Function
def main():
    if not is_solvable(CAPACITY_A, CAPACITY_B, TARGET):
        print("No solution exists for the given configuration.")
        return

    print(f"Jug A Capacity: {CAPACITY_A} liters")
    print(f"Jug B Capacity: {CAPACITY_B} liters")
    print(f"Target: {TARGET} liters\n")

    print(f"Initial State: Jug A = {initial_state[0]} liters, Jug B = {initial_state[1]} liters\n")

    solution = ida_star(initial_state, TARGET)

    if solution:
        print("Solution Found!\n")
        print_solution(solution)
    else:
        print("No solution exists for the given configuration.")

if __name__ == "__main__":
    main()
