"""8-Puzzle"""
import heapq as h

def print_state(st):
    for i in range(0,9,3):
        print(st[i], st[i+1], st[i+2])
    print()
    
def huristic(state,goal):
    distance = 0
    for i in range(1,9):
        s = state.index(i)
        g = goal.index(i)
        row1, col1 = divmod(s,3)
        row2, col2 = divmod(g,3)
        distance += abs(row1-row2) + abs(col2-col1)
    return distance

def get_next_state(state):
    next_state = []
    blank = state.index(0)
    row, col = divmod(blank,3)
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    
    for r,c in direction:
        new_row, new_col = r+row, col+c
        if 0<=new_row<3 and 0<=new_col<3:
            new_blank = new_row*3 + new_col #new index---
            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            next_state.append(tuple(new_state))
    return next_state
            
def a_star(start,goal):
    visited = set()
    pq = []
    h.heappush(pq,(0+huristic(start,goal),0,start,[]))
    while pq:
        f, g, current_state, path = h.heappop(pq)
        
        if(current_state in visited):
            continue
        visited.add(current_state)
        
        if(current_state == goal):
            print("Goal State Reached!")
            for st in path + [current_state]:
                print_state(st)
            print(goal)
            return
        
        for next_state in get_next_state(current_state):
            if next_state not in visited:
                g_cost = g + 1
                h.heappush(pq,(huristic(next_state,goal)+g_cost,g_cost,next_state,path+[current_state]))
    print("Goal not Reached")
    return None

start = (1,2,3,5,6,0,7,8,4)
goal = (1,2,3,4,5,6,7,8,0)
a_star(start,goal)