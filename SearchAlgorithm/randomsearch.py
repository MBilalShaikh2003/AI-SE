import random

graph={
    'A':['B','C'],
    'B':['A','E','D'],
    'C':['A','E'],
    'D':['B','F'],
    'E':['C','B','F'],
    'F':['E','D']
}

target_node=input("Enter Target Node (for EG A,B,C,D etc): ")

# Random Search algorithm to find the target node
def random_search(graph, start_node, target_node, max_steps):
    current_node = start_node
    steps = 0

    while steps < max_steps:
        print(f"Current node: {current_node}")  # Optional: Print the current node
        if current_node == target_node:
            return f"Target node '{target_node}' found in {steps} steps!"

        # Randomly choose a neighbor to move to
        neighbors = graph.get(current_node, [])
        if not neighbors:
            return f"Stuck at node {current_node}. Target node not found."

        current_node = random.choice(neighbors)
        steps += 1

    return f"Target node '{target_node}' not found within {max_steps} steps."

# Parameters
start_node = 'A'  # Starting node
max_steps = 20    # Maximum number of steps to search

# Run the random search
result = random_search(graph, start_node, target_node, max_steps)
print(result)











# def random_search(graph,start_node,target_node,max_steps):
#     current_node=start_node
#     steps=0
#     while steps<max_steps:
#         print(f"Current node : `{current_node}`")
#         if(current_node==target_node):
#             return f"Target node `{target_node}` found in {steps} steps" 

#         neighbours=graph.get(current_node,[])
#         if not neighbours:
#             return "Target not found"

#         current_node=random.choice(neighbours)
#         step+=1

#     return f"Target node `{target_node}` not found with in {max_steps} steps"

# start_node='A'
# max_steps=20

# result=random_search(graph,start_node,target_node,max_steps)
# print(result)













