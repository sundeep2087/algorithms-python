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
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            return True
        return False


def kruskals_mst(n, edges):
    edges.sort(key=lambda x: x[2])
    mst = []
    cost = 0
    uf = UnionFind(n)
    
    for u, v, weight in edges:
        if uf.union(u, v):
            cost += weight
            mst.append((u, v, edges))
            if len(mst) == n - 1:
                break
    
    return cost, mst


def test_case(name, n, edges, expected_cost):
    cost, mst = kruskals_mst(n, edges)
    print(f"{name}: Cost {cost}, Expected {expected_cost} - {'✓' if cost == expected_cost else '✗'}")
    assert cost == expected_cost, f"{name} failed!"
    return cost, mst

def run_tests():
    print("Running Kruskal's MST Tests")
    
    # Basic connected graph
    test_case("Basic Graph", 4, [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)], 19)
    
    # Disconnected components
    test_case("Disconnected", 5, [(0,1,1), (0,2,2), (3,4,3)], 6)
    
    # Parallel edges
    test_case("Parallel Edges", 3, [(0,1,10), (0,1,5), (1,2,3), (0,2,12)], 8)
    
    # Edge cases
    test_case("Empty Graph", 0, [], 0)
    test_case("Single Node", 1, [], 0)
    
    # Larger graph
    edges = [(0,1,7), (0,3,5), (1,2,8), (1,3,9), (1,4,7), (2,4,5), 
             (3,4,15), (3,5,6), (4,5,8), (4,6,9), (5,6,11)]
    test_case("Larger Graph", 7, edges, 39)
    
    print("All tests passed! ✓")


if __name__ == "__main__":
    run_tests()