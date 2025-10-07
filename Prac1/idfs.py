from graph import graph

def idfs(start,goal):
    visited = set()
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor in reversed(graph[node]):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

start = 'A'
goal = 'J'
path = idfs(start,goal)
print(f"{start}to{goal}:",path)
