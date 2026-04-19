from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (node, cost, stops)
        queue = deque([(src, 0, 0)])
        
        # lưu cost tốt nhất tới node với số stop cụ thể
        dist = [float('inf')] * n
        dist[src] = 0
        
        res = float('inf')
        
        while queue:
            node, cost, stops = queue.popleft()
            
            if stops > k:
                continue
            
            for nei, price in graph[node]:
                new_cost = cost + price
                
                # chỉ đi tiếp nếu tốt hơn
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    queue.append((nei, new_cost, stops + 1))
        
        return dist[dst] if dist[dst] != float('inf') else -1