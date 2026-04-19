from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # queue các node indegree = 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order) == numCourses else []