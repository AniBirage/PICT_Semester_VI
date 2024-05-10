import sys


class ConnectingCities:
    def __init__(self):
        self.graph = []
        self.parent = {}

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def find(self, city):
        if self.parent[city] != city:
            self.parent[city] = self.find(self.parent[city])
        return self.parent[city]

    def union(self, city1, city2):
        root1 = self.find(city1)
        root2 = self.find(city2)
        self.parent[root2] = root1

    def kruskal_mst(self):
        self.graph.sort(key=lambda x: x[2])
        mst = []

        for city in self.graph:
            u, v, weight = city
            if self.find(u) != self.find(v):
                mst.append(city)
                self.union(u, v)

        self.print_mst(mst)

    def print_mst(self, mst):
        print("Edge \tWeight")
        for u, v, weight in mst:
            print(u, "-", v, "\t", weight)


connecting_cities = ConnectingCities()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, weight = input("Enter edge and weight (format: City1 City2 weight): ").split()
    connecting_cities.add_edge(u, v, int(weight))
    connecting_cities.parent[u] = u
    connecting_cities.parent[v] = v

connecting_cities.kruskal_mst()
