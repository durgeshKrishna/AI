from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]

def best_first_search(source, target, n):
    visited = [False] * n
    visited[source] = True
    pq = PriorityQueue()
    pq.put((0, source))  # (cost, node)
    
    total_cost = 0  # Track the total cost
    
    while not pq.empty():
        current = pq.get()
        u = current[1]  # Get the current node
        current_cost = current[0]  # Get the cost to reach this node
        
        # Print the current node and add its cost to the total
        print(u, end=" ")
        total_cost += current_cost
        
        if u == target:
            break
        
        # Explore all the neighbors of the current node
        for v, cost in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((cost, v))  # Add neighbor to the priority queue with its cost

    print()  # Newline after printing path
    print('Total cost:', total_cost)

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# Graph structure
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

# Source and target nodes
source = 0
target = 8

# Perform best-first search and print the total cost
best_first_search(source, target, v)
