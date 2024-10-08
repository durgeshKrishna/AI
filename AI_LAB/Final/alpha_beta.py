class GraphNode:
    def __init__(self, label, is_maximizing=True, utility=None):
        self.label = label
        self.is_maximizing = is_maximizing
        self.children = []      # List to hold child GraphNode instances
        self.utility = utility  # Utility value for terminal nodes

    def add_child(self, child_node):
        self.children.append(child_node)


def minimax(node, alpha=float('-inf'), beta=float('inf'), memo=None):
    if memo is None:
        memo = {}

    # If the node's value is already computed, return it
    if node.label in memo:
        return memo[node.label]

    # If it's a terminal node, return its utility
    if node.utility is not None:
        memo[node.label] = node.utility
        return node.utility

    if node.is_maximizing:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, alpha, beta, memo)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        memo[node.label] = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, alpha, beta, memo)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        memo[node.label] = min_eval
        return min_eval


def build_sample_graph():

    # Create terminal nodes with utility values
    D = GraphNode(label='D', is_maximizing=True, utility=3)
    E = GraphNode(label='E', is_maximizing=True, utility=5)
    F = GraphNode(label='F', is_maximizing=True, utility=2)
    G = GraphNode(label='G', is_maximizing=True, utility=9)

    # Create intermediate nodes
    B = GraphNode(label='B', is_maximizing=False)  # Minimizing node
    C = GraphNode(label='C', is_maximizing=False)  # Minimizing node

    # Connect B to D and E
    B.add_child(D)
    B.add_child(E)

    # Connect C to F and G
    C.add_child(F)
    C.add_child(G)

    # Create root node A and connect to B and C
    A = GraphNode(label='A', is_maximizing=True)  # Maximizing node
    A.add_child(B)
    A.add_child(C)

    return A


def main():
    # Build the sample graph
    root = build_sample_graph()

    # Perform Minimax with Alpha-Beta Pruning on the root node
    optimal_value = minimax(root)

    # Display the result
    print(f"The optimal value for node {root.label} is: {optimal_value}")

if __name__ == "__main__":
    main()
