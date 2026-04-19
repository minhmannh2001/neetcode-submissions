class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def canReach(water_level):
            """Kiểm tra có thể đến đích với mức nước này không"""
            if grid[0][0] > water_level:
                return False
            
            visited = set([(0, 0)])
            stack = [(0, 0)]
            
            while stack:
                i, j = stack.pop()
                
                if i == n - 1 and j == n - 1:
                    return True
                
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    
                    if (0 <= ni < n and 0 <= nj < n and 
                        (ni, nj) not in visited and 
                        grid[ni][nj] <= water_level):
                        visited.add((ni, nj))
                        stack.append((ni, nj))
            
            return False
        
        # Binary search trên mức nước
        left, right = grid[0][0], n * n - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        
        return left