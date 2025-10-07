from collections import deque
from graph import graph

def bfs(start,goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    return None

start = 'A'
goal = 'J'
path = bfs(start,goal)
print(f"{start} to {goal}:",path)
