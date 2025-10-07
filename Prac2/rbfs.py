from RMP import dict_gn
from collections import deque

def recursive_bfs(queue, goal, visited):
    # Base case: If the queue is empty, the goal was not found.
    if not queue:
        return None

    # Get the current path from the front of the queue.
    path = queue.popleft()
    node = path[-1]

    # If the current node is the goal, return the path.
    if node == goal:
        return path
    
    # Mark the node as visited if it's not already.
    if node not in visited:
        visited.add(node)
        
        # Enqueue new paths for all unvisited neighbors.
        for neighbor in sorted(dict_gn.get(node, {}).keys()):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # Recursive step: continue the search with the updated queue.
    return recursive_bfs(queue, goal, visited)
start_city = 'Arad'
goal_city = 'Bucharest'
    
    # Initialize the queue with the starting
initial_queue = deque([[start_city]])
    
    # Initialize a set to keep track of visited cities.
visited_nodes = set()
    
path = recursive_bfs(initial_queue, goal_city, visited_nodes)
    
if path:
    print(f"Recursive BFS Path from {start_city} to {goal_city}:")
    print(" -> ".join(path))
    print(f"(This path has the fewest city stops: {len(path) - 1} stops)")
else:
    print(f"No path found from {start_city} to {goal_city}.")
