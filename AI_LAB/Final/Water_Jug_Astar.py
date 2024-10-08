import heapq as h

def huristic(x,y,g):
    return min(abs(x-g),abs(y-g))

def water_jug_Astar(j1,j2,goal):
    visited = set()
    pq = []
    x = 0
    y = 0
    parent = {(x,y) : (-1,-1)}
    g_cost = {(x,y) : (0, 0)}
    h.heappush(pq,(huristic(x,y,goal),0,x,y))
    while pq:
        f_cost, current_g_cost, x, y = h.heappop(pq);
        if((x,y) in visited):
            continue
        visited.add((x,y))
        
        if(x == goal or y == goal):
            path = []
            while((x,y) != (-1,-1)):
                path.append((x,y))
                (x,y) = parent[(x,y)]
            path.reverse()
            print(path)
            print("Path Found")
            return
        next_state = [
            (j1,y),
            (x,j2),
            (0,y),
            (x,0),
            (min(j1,x+y),max(0,y - (j1-x))),
            (max(0,x - (j2-y)),min(j2,x+y)),
        ]
        for next_x,next_y in next_state:
            if (next_x,next_y) not in visited:
                new_g_cost = current_g_cost + 1
                if (next_x,next_y) not in g_cost or new_g_cost < g_cost[(next_x,next_y)]:
                    parent[(next_x,next_y)] = (x,y)
                    g_cost[(next_x,next_y)] = new_g_cost
                    h.heappush(pq,(huristic(next_x,next_y,goal)+new_g_cost,new_g_cost,next_x,next_y))
    print("Not Reached")
    return None
        

j1 = int(input("Jug1: "))
j2 = int(input("Jug2: "))
goal = int(input("Amt. to be measured: "))
water_jug_Astar(j1,j2,goal)