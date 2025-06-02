from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.parent[x]
        root_y = self.parent[y]
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def find_connected_components(n, edges):
    uf = UnionFind(n)
    
    # Find union of connected components
    for u, v in edges:
        uf.union(u, v)
    
    # Collect sets of connceted components
    components = defaultdict(list)
    for node in range(n):
        root = uf.find(node)
        components[root].append(node)
    return components


if __name__ == "__main__":
    edgelist1= [[0, 1], [2, 1], [0, 3], [3, 4], [5, 6], [7, 8], [5, 8]]
    edgelist2= [[0, 1], [2, 1], [3, 4], [5, 6]]
    edgelists = [
        (9, edgelist1), 
        (7, edgelist2)
    ]
    for n, edges in edgelists:
        connected_components = find_connected_components(n, edges)
        print(connected_components)