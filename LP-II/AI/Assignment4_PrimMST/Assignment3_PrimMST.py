import sys


class ConnectingCities:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in key:
            if key[v] < min_val and mst_set[v] is False:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = {v: sys.maxsize for v in self.graph}
        parent = {v: None for v in self.graph}
        key[next(iter(self.graph))] = 0
        mst_set = {v: False for v in self.graph}

        for _ in range(len(self.graph)):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in self.graph[u]:
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for v in self.graph:
            if parent[v] is not None:
                print(parent[v], "-", v, "\t", self.graph[v][parent[v]])


connecting_cities = ConnectingCities()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, weight = input("Enter edge and weight (format: City1 City2 weight): ").split()
    connecting_cities.add_edge(u, v, int(weight))

connecting_cities.prim_mst()
