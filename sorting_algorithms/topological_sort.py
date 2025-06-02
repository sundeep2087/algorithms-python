from collections import deque, defaultdict
from typing import Optional

class TopologicalSort:
    def khans_bfs(self, graph: dict[str, list]):
        indegree = defaultdict(int)
        
        # Calculate indegrees
        for vertex in graph:
            if vertex not in indegree:
                indegree[vertex] = 0
            for neighbor in graph[vertex]:
                indegree[neighbor] += 1
        
        # Pick vertices with 0 indegree
        queue = deque()
        for vertex in graph.keys():
            if indegree[vertex] == 0:
                queue.append(vertex)
        
        result = []
        # Iteratively process vertices of 0 indegree
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != len(indegree):
            raise ValueError("Contains Cycle. Not a DAG.")
        return result
                
        


if __name__ == "__main__":
    ts = TopologicalSort()
    graph1 = {
        'Math': ['Physics', 'Chemistry'], 
        'Physics': ['Engineering'], 
        'Chemistry': ['Biology'], 
        'Engineering': [], 
        'Biology': []
    }
    
    # Test Case 2: Linear Chain DAG
    graph2 = {
        'A': ['B'], 
        'B': ['C'], 
        'C': ['D'], 
        'D': []
    }
    
    # Test Case 3: Complex DAG - Build Dependencies
    graph3 = {
        'main.cpp': ['compile'], 
        'utils.cpp': ['compile'], 
        'compile': ['link'], 
        'config.h': ['compile'], 
        'link': ['package'], 
        'package': []
    }
    
    # Test Case 4: Simple Cycle
    graph4 = {
        'A': ['B'], 
        'B': ['C'], 
        'C': ['A']
    }
    
    # Test Case 5: Self Loop
    graph5 = {
        'A': ['A', 'B'], 
        'B': []
    }
    
    # Test Case 6: Complex Cycle
    graph6 = {
        'X': ['Y'], 
        'Y': ['Z'], 
        'Z': ['W'], 
        'W': ['X'], 
        'A': ['B'], 
        'B': []
    }
    
    # Test Case 7: Single Node
    graph7 = {'A': []}
    
    # Test Case 8: Disconnected DAG
    graph8 = {
        'A': ['B'], 
        'B': [], 
        'C': ['D'], 
        'D': []
    }
    
    test_cases = [
        (graph1, "Course Prerequisites DAG"),
        (graph2, "Linear Chain DAG"),
        (graph3, "Build Dependencies DAG"),
        (graph4, "Simple Cycle"),
        (graph5, "Self Loop"),
        (graph6, "Complex Cycle"),
        (graph7, "Single Node"),
        (graph8, "Disconnected DAG")
    ]
    
    for graph, description in test_cases:
        try:
            result = ts.khans_bfs(graph)
            print(f"{description}: {result}")
        except ValueError as e:
            print(f"{description} Error - {e}")
            