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


# graph.py

class Graph:
    """Base Graph class for creating general graph structures using an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def remove_node(self, node):
        """Remove a node and all associated edges from the graph."""
        if node in self.graph:
            del self.graph[node]
            # Remove this node from all other nodes' adjacency lists
            for adj_list in self.graph.values():
                if node in adj_list:
                    adj_list.remove(node)

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2. To be overridden in subclasses."""
        pass

    def remove_edge(self, node1, node2):
        """Remove an edge between node1 and node2. To be overridden in subclasses."""
        pass

    def get_neighbors(self, node):
        """Return the neighbors of a node."""
        return self.graph.get(node, [])

    def has_edge(self, node1, node2):
        """Check if there is an edge between node1 and node2."""
        return node2 in self.graph.get(node1, [])

    def display_graph(self):
        """Display the graph as an adjacency list."""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    def n_vertices(self):
        return len(self.graph)

    def get_nodes(self):
        return self.graph.keys()


class DirectedGraph(Graph):
    """Directed Graph class, inheriting from Graph."""

    def add_edge(self, node1, node2):
        """Add a directed edge from node1 to node2."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)

    def remove_edge(self, node1, node2):
        """Remove the directed edge from node1 to node2."""
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)


class UndirectedGraph(Graph):
    """Undirected Graph class, inheriting from Graph."""

    def add_edge(self, node1, node2):
        """Add an undirected edge between node1 and node2."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_edge(self, node1, node2):
        """Remove the undirected edge between node1 and node2."""
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        if node2 in self.graph and node1 in self.graph[node2]:
            self.graph[node2].remove(node1)


class WeightedDirectedGraph(DirectedGraph):
    """Weighted Directed Graph class, inheriting from DirectedGraph."""

    def add_edge(self, node1, node2, weight):
        """Add a directed edge from node1 to node2 with a weight."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append((node2, weight))

    def remove_edge(self, node1, node2):
        """Remove the directed edge from node1 to node2."""
        if node1 in self.graph:
            self.graph[node1] = [n for n in self.graph[node1] if n[0] != node2]

    def get_edge_weight(self, node1, node2):
        """Get the weight of the directed edge from node1 to node2."""
        if node1 in self.graph:
            for neighbor, weight in self.graph[node1]:
                if neighbor == node2:
                    return weight
        return None


class WeightedUndirectedGraph(UndirectedGraph):
    """Weighted Undirected Graph class, inheriting from UndirectedGraph."""

    def add_edge(self, node1, node2, weight):
        """Add an undirected edge between node1 and node2 with a weight."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def remove_edge(self, node1, node2):
        """Remove the undirected edge between node1 and node2."""
        if node1 in self.graph:
            self.graph[node1] = [n for n in self.graph[node1] if n[0] != node2]
        if node2 in self.graph:
            self.graph[node2] = [n for n in self.graph[node2] if n[0] != node1]

    def get_edge_weight(self, node1, node2):
        """Get the weight of the undirected edge between node1 and node2."""
        if node1 in self.graph:
            for neighbor, weight in self.graph[node1]:
                if neighbor == node2:
                    return weight
        return None



if __name__ == "__main__":
    # Create a Directed Graph
    directed_graph = DirectedGraph()
    directed_graph.add_edge('A', 'B')
    directed_graph.add_edge('B', 'A')
    directed_graph.add_edge('B', 'C')
    directed_graph.add_edge('C', 'A')
    directed_graph.display_graph()
    print("\n\n")

    # Create an Undirected Graph
    undirected_graph = UndirectedGraph()
    undirected_graph.add_edge('A', 'B')
    undirected_graph.add_edge('B', 'C')
    undirected_graph.add_edge('C', 'A')
    undirected_graph.display_graph()
    print("\n\n")

    # Create a Weighted Directed Graph
    weighted_directed_graph = WeightedDirectedGraph()
    weighted_directed_graph.add_edge('A', 'B', 5)
    weighted_directed_graph.add_edge('B', 'C', 10)
    weighted_directed_graph.add_edge('C', 'A', 15)
    weighted_directed_graph.display_graph()
    print("\n\n")

    # Create a Weighted Undirected Graph
    weighted_undirected_graph = WeightedUndirectedGraph()
    weighted_undirected_graph.add_edge('A', 'B', 5)
    weighted_undirected_graph.add_edge('B', 'C', 10)
    weighted_undirected_graph.add_edge('C', 'A', 15)
    weighted_undirected_graph.display_graph()