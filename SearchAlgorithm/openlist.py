from collections import deque

# Define a graph as a dictionary (adjacency list)

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

# Open List Search (BFS-like approach)
def open_list_search(graph, start_node, target_node):
    open_list = deque()  # Queue for nodes to explore
    closed_list = set()  # Set to keep track of visited nodes

    # Initialize the open list with the start node
    open_list.append(start_node)

    while open_list:
        # Get the next node from the open list
        current_node = open_list.popleft()
        print(f"Exploring node: {current_node}")  # Optional: Print the current node

        # Check if the current node is the target
        if current_node == target_node:
            return f"Target node '{target_node}' found!"

        # Add the current node to the closed list
        closed_list.add(current_node)

        # Add unvisited neighbors to the open list
        for neighbor in graph.get(current_node, []):
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)

    return f"Target node '{target_node}' not found."

# Parameters
start_node = 'A'  # Starting node

# Run the open list search
result = open_list_search(graph, start_node, target_node)
print(result)