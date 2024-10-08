import heapq
def heuristic(jug1, jug2, goal, target_jug):
    if target_jug == 1:
        return abs(jug1 - goal)
    else:
        return abs(jug2 - goal)
def is_goal(state, goal, target_jug):
    jug1, jug2 = state
    if target_jug == 1:
        return jug1 == goal
    else:
        return jug2 == goal

def best_first_search(jug1_capacity, jug2_capacity, goal, target_jug):
    pq = [] 
    start_state = (0, 0) 
    heapq.heappush(pq, (heuristic(0, 0, goal, target_jug), start_state, [])) 
    visited = set() 
    
    while pq:
        _, current_state, path = heapq.heappop(pq)
        
        if is_goal(current_state, goal, target_jug):
            return path + [current_state]
        
        if current_state in visited:
            continue
        
        visited.add(current_state) 
        jug1, jug2 = current_state  
        next_states = []
        next_states.append((jug1_capacity, jug2))
        next_states.append((jug1, jug2_capacity))
        next_states.append((0, jug2))
        next_states.append((jug1, 0))
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
        
        for state in next_states:
            if state not in visited:
                h = heuristic(state[0], state[1], goal, target_jug) 
                heapq.heappush(pq, (h, state, path + [current_state])) 

    return None 
jug1_capacity = int(input("Enter capacity of Jug 1: "))  
jug2_capacity = int(input("Enter capacity of Jug 2: "))
goal = int(input("Enter the goal amount of water: ")) 
target_jug = int(input("Which jug should contain the goal (1 or 2): "))
solution = best_first_search(jug1_capacity, jug2_capacity, goal, target_jug)
if solution:
    print("Solution path:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
