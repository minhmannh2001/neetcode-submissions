from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        @lru_cache(None)
        def dfs(i, j):
            res = 1  # ít nhất là chính nó
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            
            return res
        
        return max(dfs(i, j) for i in range(m) for j in range(n))