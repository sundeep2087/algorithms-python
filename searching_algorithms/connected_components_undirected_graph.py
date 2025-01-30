"""
Author: Sai Sundeep Rayidi
Date: 12/24/2024

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


from advanced_data_structures.graph_adjacency_list import UndirectedGraph
from intermediate_data_structures.queue_adt_node_implementation import LLQueue


def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph.get_neighbors(node):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)


def find_connected_components(graph):
    visited = set()
    connected_components = []

    for node in graph.get_nodes():
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            connected_components.append(component)

    return connected_components


if __name__ == "__main__":
    graph = UndirectedGraph()

    # # Add Nodes
    # graph.add_node('r')
    # graph.add_node('s')
    # graph.add_node('t')
    # graph.add_node('u')
    # graph.add_node('v')
    # graph.add_node('w')
    # graph.add_node('x')
    # graph.add_node('y')
    #
    # # Add Edges
    # graph.add_edge("r", "v")
    # graph.add_edge("r", "s")
    # graph.add_edge("s", "w")
    # graph.add_edge("w", "t")
    # graph.add_edge("w", "x")
    # graph.add_edge("x", "t")
    # graph.add_edge("u", "t")
    # graph.add_edge("x", "u")
    # graph.add_edge("y", "x")
    # graph.add_edge("y", "u")

    n = 7
    for i in range(n):
        graph.add_node(i)

    edges = [[0,1], [0,2], [1,0], [1,2], [2,1], [2,0], [3,4], [5,6]]
    for u, v in edges:
        graph.add_edge(u, v)

    connected_components = find_connected_components(graph)
    print(connected_components)

