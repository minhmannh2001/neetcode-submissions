from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        pacific = [[None] * cols for _ in range(rows)]
        atlantic = [[None] * cols for _ in range(rows)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, ocean, visiting):
            # nếu đã tính rồi
            if ocean[r][c] is not None:
                return ocean[r][c]
            
            # nếu đang visit → tránh cycle
            if (r, c) in visiting:
                return False
            
            visiting.add((r, c))
            
            # check border
            if ocean is pacific and (r == 0 or c == 0):
                ocean[r][c] = True
            elif ocean is atlantic and (r == rows - 1 or c == cols - 1):
                ocean[r][c] = True
            else:
                ocean[r][c] = False
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] <= heights[r][c]:
                            if dfs(nr, nc, ocean, visiting):
                                ocean[r][c] = True
                                break
            
            visiting.remove((r, c))
            return ocean[r][c]
        
        result = []
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, pacific, set()) and dfs(r, c, atlantic, set()):
                    result.append([r, c])
        
        return result