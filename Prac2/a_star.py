import heapq
from RMP import dict_gn,dict_hn

def a_star_search(start, goal):
    # Priority queue storing tuples of (f_cost, g_cost, path)
    # f_cost is the priority: f(n) = g(n) + h(n)
    priority_queue = [(dict_hn[start], 0, [start])]
    
    # A dictionary to keep track of the minimum g_cost found so far for each city
    visited_costs = {start: 0}

    while priority_queue:
        # Pop the path with the smallest f_cost
        f_cost, g_cost, path = heapq.heappop(priority_queue)
        
        node = path[-1]

        # If we reached the goal, we are done
        if node == goal:
            return path, g_cost

        # Explore neighbors
        for neighbor, distance in dict_gn.get(node, {}).items():
            new_g_cost = g_cost + distance
            
            # If we found a shorter path to the neighbor, update it
            if neighbor not in visited_costs or new_g_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_g_cost
                new_f_cost = new_g_cost + dict_hn.get(neighbor, float('inf'))
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_f_cost, new_g_cost, new_path))
    
    return None, None

start_city = 'Arad'
goal_city = 'Bucharest'
    
path, total_cost = a_star_search(start_city, goal_city)
    
if path:
    print(f"A* Search Path from {start_city} to {goal_city}:")
    print(" -> ".join(path))
    print(f"Total distance: {total_cost} km")
else:
    print(f"No path found from {start_city} to {goal_city}.")
