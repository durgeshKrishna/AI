import math

def Min_Max_AlphaBeta(cd, node, maxt, src, td, alpha, beta, depth=0):
    if cd == td:
        return src[node]
    
    indent = "  " * depth
    if maxt:
        max_val = float('-inf')
        # Explore left child
        val = Min_Max_AlphaBeta(cd + 1, node * 2, False, src, td, alpha, beta, depth + 1)
        max_val = max(max_val, val)
        alpha = max(alpha, val)
        if beta <= alpha:
            print(f"{indent}Pruning at node {node * 2 + 1} (maximizing, depth {cd + 1})")
            return max_val
        # Explore right child
        val = Min_Max_AlphaBeta(cd + 1, node * 2 + 1, False, src, td, alpha, beta, depth + 1)
        max_val = max(max_val, val)
        alpha = max(alpha, val)
        if beta <= alpha:
            print(f"{indent}Pruning at node {node * 2 + 1} (maximizing, depth {cd + 1})")
            return max_val
        return max_val
    else:
        min_val = float('inf')
        # Explore left child
        val = Min_Max_AlphaBeta(cd + 1, node * 2, True, src, td, alpha, beta, depth + 1)
        min_val = min(min_val, val)
        beta = min(beta, val)
        if beta <= alpha:
            print(f"{indent}Pruning at node {node * 2 + 1} (minimizing, depth {cd + 1})")
            return min_val
        # Explore right child
        val = Min_Max_AlphaBeta(cd + 1, node * 2 + 1, True, src, td, alpha, beta, depth + 1)
        min_val = min(min_val, val)
        beta = min(beta, val)
        if beta <= alpha:
            print(f"{indent}Pruning at node {node * 2 + 1} (minimizing, depth {cd + 1})")
            return min_val
        return min_val

# Input leaf nodes
src = list(map(int, input("leaf nodes: ").split()))
td = math.ceil(math.log2(len(src)))

cd = 0
node = 0
maxt = True
alpha = float('-inf')
beta = float('inf')
answer = Min_Max_AlphaBeta(cd, node, maxt, src, td, alpha, beta)
print("Optimal Val:", answer)
