from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        count = 0

        for i in range(n):
            if visited[i]:
                continue

            # tìm thấy 1 component mới
            count += 1

            # BFS
            queue = deque([i])
            visited[i] = True

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)

        return count