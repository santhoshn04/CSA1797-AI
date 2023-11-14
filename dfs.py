from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
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
    visited_nodes = set()
    print(f"DFS traversal from node {start_node}:")
    graph.dfs(start_node, visited_nodes)
if __name__ == "__main__":
    main()
