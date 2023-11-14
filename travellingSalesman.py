import sys
class TravelingSalesman:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.adj_matrix = [[0] * num_cities for _ in range(num_cities)]
        self.visited = [False] * num_cities
    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
    def nearest_neighbor(self, start_city):
        self.visited[start_city] = True
        tour = [start_city]
        total_distance = 0
        current_city = start_city
        for _ in range(self.num_cities - 1):
            nearest_city = self.find_nearest_city(current_city)
            tour.append(nearest_city)
            total_distance += self.adj_matrix[current_city][nearest_city]
            self.visited[nearest_city] = True
            current_city = nearest_city
        tour.append(start_city)
        total_distance += self.adj_matrix[current_city][start_city]
        return tour, total_distance
    def find_nearest_city(self, city):
        min_distance = sys.maxsize
        nearest_city = -1
        for i in range(self.num_cities):
            if not self.visited[i] and self.adj_matrix[city][i] < min_distance:
                min_distance = self.adj_matrix[city][i]
                nearest_city = i
        return nearest_city
def main():
    num_cities = 5
    tsp = TravelingSalesman(num_cities)
    distances = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 40, 45],
        [15, 35, 0, 50, 55],
        [20, 40, 50, 0, 65],
        [25, 45, 55, 65, 0]
    ]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            tsp.add_edge(i, j, distances[i][j])
    start_city = 0
    tour, total_distance = tsp.nearest_neighbor(start_city)
    print("Nearest Neighbor TSP Solution:")
    print("Tour:", tour)
    print("Total Distance:", total_distance)
if __name__ == "__main__":
    main()
