class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Bước 1: lấy danh sách tất cả ô đất
        land_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    land_cells.append((r, c))

        # set lưu các ô đã được duyệt qua
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0':
                return
            if (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Bước 2: duyệt qua từng ô đất
        for (r, c) in land_cells:
            # ô này đã thuộc đảo nào đó rồi → bỏ qua
            if (r, c) in visited:
                continue

            # ô chưa được thăm → đảo mới!
            dfs(r, c)
            islands += 1

        return islands