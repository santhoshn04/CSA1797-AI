import heapq
movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
def astar(start, goal, grid):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}
    while open_set:
        _, current_node = heapq.heappop(open_set)
        if current_node == goal:
            path = reconstruct_path(current_node)
            return path
        closed_set.add(current_node)
        for movement in movements:
            neighbor = (current_node[0] + movement[0], current_node[1] + movement[1])
            if neighbor not in grid or neighbor in closed_set:
                continue
            tentative_g_score = g_score[current_node] + 1

            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None
def reconstruct_path(node):
    path = [node]
    while node in came_from:
        node = came_from[node]
        path.insert(0, node)
    return path
grid = set([(0, 1), (1, 1), (2, 1), (3, 1)])
start = (0, 0)
goal = (3, 3)
path = astar(start, goal, grid)
if path:
    print("Shortest Path:", path)
else:
    print("No path found!")
