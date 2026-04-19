from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (cost, node, stops)
        heap = [(0, src, 0)]
        
        # dist[node][stops] = min cost
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # tới đích luôn return (vì heap đảm bảo cost nhỏ nhất)
            if node == dst:
                return cost
            
            # nếu vượt quá stops
            if stops > k:
                continue
            
            for nei, price in graph[node]:
                new_cost = cost + price
                
                if new_cost < dist[nei][stops + 1]:
                    dist[nei][stops + 1] = new_cost
                    heapq.heappush(heap, (new_cost, nei, stops + 1))
        
        return -1