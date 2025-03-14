import random

graph={
    'A':['B','C'],
    'B':['A','E','D'],
    'C':['A','E'],
    'D':['B','F'],
    'E':['C','B','F'],
    'F':['E','D']
}

# Target node to find
target_node = 'F'

# Random Search algorithm with a closed list (visited nodes)
def random_search_with_closed_list(graph, start_node, target_node, max_steps):
    current_node = start_node
    steps = 0
    closed_list = set()  # Set to keep track of visited nodes

    while steps < max_steps:
        print(f"Current node: {current_node}")  # Optional: Print the current node
        if current_node == target_node:
            return f"Target node '{target_node}' found in {steps} steps!"

        # Add the current node to the closed list
        closed_list.add(current_node)

        # Get the neighbors of the current node that haven't been visited
        neighbors = [node for node in graph.get(current_node, []) if node not in closed_list]

        if not neighbors:
            return f"Stuck at node {current_node}. Target node not found."

        # Randomly choose a neighbor to move to
        current_node = random.choice(neighbors)
        steps += 1

    return f"Target node '{target_node}' not found within {max_steps} steps."

# Parameters
start_node = 'A'  # Starting node
max_steps = 20    # Maximum number of steps to search

# Run the random search with a closed list
result = random_search_with_closed_list(graph, start_node, target_node, max_steps)
print(result)