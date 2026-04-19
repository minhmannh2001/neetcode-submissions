from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        # Bước 1: lấy ra tất cả điểm kho báu
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))   # (row, col, distance)

        # Bước 2: BFS từ TẤT CẢ kho báu cùng lúc
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))