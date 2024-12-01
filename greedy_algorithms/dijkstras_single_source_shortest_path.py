"""
Author: Sai Sundeep Rayidi
Date: 11/30/2024

Description:
[Description of what the file does, its purpose, etc.]

Additional Notes:
[Any additional notes or information you want to include.]

License: 
MIT License

Copyright (c) 2024 Sai Sundeep Rayidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact:
[Optional: How to reach you for questions or collaboration.]

"""

from advanced_data_structures.graph_adjacency_list import WeightedUndirectedGraph
import heapq


def dijkstras_single_source_shortest_path(graph, source):
    min_heap = []
    heapq.heappush(min_heap, (0, source))
    visited_nodes = set()
    distances_array = [float("inf")] * graph.n_vertices()
    distances_array[source] = 0

    while min_heap:
        d, u = heapq.heappop(min_heap)
        if u not in visited_nodes:
            visited_nodes.add(u)

        for v, weight in graph.get_neighbors(u):
            if v not in visited_nodes and (distances_array[v] > distances_array[u] + weight):
                distances_array[v] = distances_array[u] + weight
                heapq.heappush(min_heap, (distances_array[v], v))

    return distances_array


def check_dssp():
    graph = WeightedUndirectedGraph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)
    graph.add_node(7)
    graph.add_node(8)
    graph.add_node(0)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    distances = dijkstras_single_source_shortest_path(graph, 0)
    for v in range(graph.n_vertices()):
        print(f"Node: {v} | Distance: {distances[v]}")


if __name__ == "__main__":
    check_dssp()