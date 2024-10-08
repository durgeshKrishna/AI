class GraphNode:
    def __init__(self, label, is_maximizing=True, utility=None):
        self.label = label
        self.is_maximizing = is_maximizing
        self.children = []      # List to hold child GraphNode instances
        self.utility = utility  # Utility value for terminal nodes

    def add_child(self, child_node):
        self.children.append(child_node)


def minimax(node, memo=None):
    if memo is None:
        memo = {}

    # If the node's value is already computed, return it
    if node.label in memo:
        return memo[node.label]

    # If it's a terminal node, return its utility
    if node.utility is not None:
        memo[node.label] = node.utility
        return node.utility

    # Initialize best_value based on whether it's a maximizing or minimizing node
    if node.is_maximizing:
        best_value = float('-inf')  # Start with the lowest possible value
        for child in node.children:
            value = minimax(child, memo)  # Recursively evaluate child
            best_value = max(best_value, value)  # Choose the maximum value
    else:
        best_value = float('inf')  # Start with the highest possible value
        for child in node.children:
            value = minimax(child, memo)  # Recursively evaluate child
            best_value = min(best_value, value)  # Choose the minimum value

    # Memoize the computed value
    memo[node.label] = best_value
    return best_value


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

    # Perform Minimax on the root node
    optimal_value = minimax(root)

    # Display the result
    print(f"The optimal value for node {root.label} is: {optimal_value}")

if __name__ == "__main__":
    main()
