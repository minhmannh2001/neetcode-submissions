from typing import List
from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def bfs(start, target):
            visited = set()
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                if node == target:
                    return True
                
                visited.add(node)
                
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
            
            return False
        
        for a, b in edges:
            # chỉ check khi cả 2 node đã có trong graph
            if a in graph and b in graph:
                if bfs(a, b):
                    return [a, b]
            
            graph[a].append(b)
            graph[b].append(a)