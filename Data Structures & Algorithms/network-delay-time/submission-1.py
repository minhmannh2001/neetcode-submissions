from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        # dist array
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        visited = [False] * (n + 1)
        
        for _ in range(n):
            # tìm node chưa visited có dist nhỏ nhất
            min_dist = float('inf')
            node = -1
            
            for i in range(1, n + 1):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    node = i
            
            # không còn node reachable
            if node == -1:
                break
            
            visited[node] = True
            
            # relax neighbors
            for nei, w in graph[node]:
                if not visited[nei]:
                    dist[nei] = min(dist[nei], dist[node] + w)
        
        # check
        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1