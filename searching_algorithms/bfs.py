"""
Author: Sai Sundeep Rayidi
Date: 12/21/2024

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
from collections import deque

# def bfs(graph, start_node):
#     """
#     :param graph: Adjacency List representation of Graph
#     :param start_node: Start Vertex in the graph
#     :return: None
#
#     This function implementation Breadth First Search (BFS) traversal of a graph.
#     It uses queue data structure to implement the BFS algorithm
#     """
#     visited = set()
#     queue = LLQueue()
#     queue.enqueue(start_node)
#     visited.add(start_node)
#
#     while not queue.is_empty():
#         curr_node = queue.dequeue()
#         print(curr_node, end=" ")
#
#         for neighbor in graph.get_neighbors(curr_node):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.enqueue(neighbor)


def bfs(graph, start_node):
    """
    :param graph:
    :param start_node:
    :return:

     This function implementation Breadth First Search (BFS) traversal of a graph.
     It uses deque from collections framweork to implement the BFS algorithm

     Pseudocode:
     Create a set("visited") to store the vertices as they are traversed
     create a deque and add the start node to the queue
     Add start node to the visited queue

     while queue is not empty:
        pop from front a vertex from the deque, let us call this curr_vertex
        print/process the vertex

        for each neighbor of curr_vertex:
            if neighbor is not in visited
                Add neighbor to visited set
                Add neighbor to the deque
    """

    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        curr_node = queue.popleft()
        print(curr_node, end=" ")

        for neighbor in graph.get_neighbors(curr_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


if __name__ == "__main__":
    # graph = UndirectedGraph()
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
    #
    # # Display Graph
    # graph.display_graph()
    # bfs(graph, 's')


    graph = UndirectedGraph()
    # Add Nodes
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)
    graph.add_node(7)

    # Add Edges
    graph.add_edge(0, 2)
    graph.add_edge(0, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(3, 5)
    graph.add_edge(3, 7)
    graph.add_edge(5, 7)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    graph.add_edge(6, 4)

    graph.display_graph()
    bfs(graph, 0)
