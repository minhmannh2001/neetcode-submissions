from typing import List
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # điều kiện cần
        if len(edges) != n - 1:
            return False
        
        # build graph
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        queue = deque([0])
        
        # BFS
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        
        return len(visited) == n