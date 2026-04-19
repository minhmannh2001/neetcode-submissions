from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(src, target, visited):
            if src == target:
                return True
            
            visited.add(src)
            
            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            
            return False
        
        for a, b in edges:
            visited = set()
            
            # nếu đã có path từ a → b thì thêm edge này sẽ tạo cycle
            if a in graph and b in graph and dfs(a, b, visited):
                return [a, b]
            
            graph[a].append(b)
            graph[b].append(a)