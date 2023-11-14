from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self, start, target):
        visited = set()
        queue = deque([(start, [])])  
        while queue:
            node, path = queue.popleft()
            visited.add(node)
            if node == target:
                return path + [node]
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [node]))
        return None
def main():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(4, 8)
    graph.add_edge(5, 9)
    start_node = 1
    target_node = 9
    path = graph.bfs(start_node, target_node)
    if path:
        print(f"Shortest path from {start_node} to {target_node}: {path}")
    else:
        print(f"No path found from {start_node} to {target_node}")
if __name__ == "__main__":
    main()
