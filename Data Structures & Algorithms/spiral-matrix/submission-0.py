class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # 4 hướng: phải, xuống, trái, lên
        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        dir_idx = 0

        visited = set()

        r = 0
        c = 0

        result = []

        for _ in range(rows * cols):
            result.append(matrix[r][c])
            visited.add((r, c))

            dr, dc = dirs[dir_idx]

            nr = r + dr
            nc = c + dc

            # nếu bước tiếp theo không hợp lệ
            if (
                nr < 0 or nr >= rows or
                nc < 0 or nc >= cols or
                (nr, nc) in visited
            ):
                # đổi hướng
                dir_idx = (dir_idx + 1) % 4

                dr, dc = dirs[dir_idx]

                nr = r + dr
                nc = c + dc

            r, c = nr, nc

        return result