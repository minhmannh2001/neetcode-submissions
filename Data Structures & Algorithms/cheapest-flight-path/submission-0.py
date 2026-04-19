from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        self.res = float('inf')
        
        def dfs(node, cost, stops, visited):
            # vượt quá stops
            if stops > k + 1:   # edges = stops + 1
                return
            
            # pruning theo cost
            if cost >= self.res:
                return
            
            # tới đích
            if node == dst:
                self.res = min(self.res, cost)
                return
            
            for nei, price in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, cost + price, stops + 1, visited)
                    visited.remove(nei)
        
        dfs(src, 0, 0, set([src]))
        
        return self.res if self.res != float('inf') else -1