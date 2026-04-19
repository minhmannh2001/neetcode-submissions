from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # queue các node có indegree = 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        
        # BFS
        while queue:
            node = queue.popleft()
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses