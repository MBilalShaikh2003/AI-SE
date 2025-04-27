import itertools

def tsp(graph, start):
    # Get all cities except the starting city
    cities = list(graph.keys())
    cities.remove(start)
    
    min_path = None
    min_cost = float('inf')
    print(cities)
    # Generate all permutations of cities
    for permutation in itertools.permutations(cities):
        
        current_cost = 0
        current_path = [start]
        current_city = start
        
        # Calculate cost for this permutation
        for next_city in permutation:
            current_cost += graph[current_city][next_city]
            current_path.append(next_city)
            current_city = next_city
        
        # Return to start
        current_cost += graph[current_city][start]
        current_path.append(start)
        
        # Update minimum if found
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path
    
    return min_path, min_cost

# Example graph from the lab (1-2-4-3-1 with cost 80)
graph_example = {
    1: {1: 0, 2: 10, 3: 15, 4: 20},
    2: {1: 10, 2: 0, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 3: 0, 4: 30},
    4: {1: 20, 2: 25, 3: 30, 4: 0}
}

path, cost = tsp(graph_example, 1)
print("Minimum weight Hamiltonian Cycle:")
print(" -> ".join(map(str, path)))
print(f"Total cost: {cost}")