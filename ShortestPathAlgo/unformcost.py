import heapq

# Define a graph as a dictionary (adjacency list with weights)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Dijkstra's algorithm
def dijkstra(graph, start_node, target_node):
    # Priority queue to store (distance, node) pairs
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph}

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Stop if we've reached the target node
        if current_node == target_node:
            # Reconstruct the shortest path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.reverse()
            return f"Shortest path to '{target_node}': {path}, Distance: {distances[target_node]}"

        # Skip if we've already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return f"No path found to '{target_node}'."

# Parameters
start_node = 'A'  # Starting node
target_node = 'F'  # Target node

# Run Dijkstra's algorithm
result = dijkstra(graph, start_node, target_node)
print(result)