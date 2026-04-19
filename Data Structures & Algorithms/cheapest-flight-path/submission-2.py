from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue = deque([(src, 0, 0)])
        
        # dist[node][stops]
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        
        while queue:
            node, cost, stops = queue.popleft()
            
            if stops > k:
                continue
            
            for nei, price in graph[node]:
                new_cost = cost + price
                
                if new_cost < dist[nei][stops + 1]:
                    dist[nei][stops + 1] = new_cost
                    queue.append((nei, new_cost, stops + 1))
        
        res = min(dist[dst])
        return res if res != float('inf') else -1