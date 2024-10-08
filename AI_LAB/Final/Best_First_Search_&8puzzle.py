import heapq as h

def huristic(state, goal):
    distance = 0
    for i in range(1, 9):
        current_index = state.index(i)
        goal_index = goal.index(i)
        current_row, current_col = divmod(current_index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_next_states(state):
    next_states = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
            next_states.append(tuple(new_state))
    
    return next_states

def print_state(st):
    for i in range(0,9,3):
        print(st[i], st[i+1], st[i+2])
    print()

def best_fs(start, goal):
    visited = set()
    pq = []
    h.heappush(pq, (huristic(start,goal), start, []))
    
    while pq:
        h_cost, current_state, path = h.heappop(pq)
        if(current_state in visited):
            continue
        visited.add(current_state)
        
        if(current_state == goal):
            print("Goal State Achieved!")
            print_state(current_state)
            return path
        
        for next_state in get_next_states(current_state):
            if(next_state not in visited):
                h.heappush(pq, (huristic(next_state,goal), next_state, path + [current_state]))

    print("Goal state not Acheived")
    return None

#start = (1, 2, 3, 4, 5, 6, 8, 0, 7)  # Example start state
start = (1, 2, 3, 5, 6, 0, 7, 8, 4)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
best_fs(start,goal)