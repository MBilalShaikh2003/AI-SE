from collections import deque

# Define a graph as a dictionary (adjacency list)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

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

# BFS algorithm
def bfs(graph, start_node, target_node):
    queue = deque()  # Queue for nodes to explore
    visited = set()  # Set to keep track of visited nodes

    # Initialize the queue with the start node
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        # Get the next node from the queue
        current_node = queue.popleft()
        print(f"Exploring node: {current_node}")  # Optional: Print the current node

        # Check if the current node is the target
        if current_node == target_node:
            return f"Target node '{target_node}' found!"

        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return f"Target node '{target_node}' not found."

# Parameters
start_node = 'A'  # Starting node

# Run the BFS algorithm
result = bfs(graph, start_node, target_node)
print(result)