"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        # prefix[r][c] = tổng số lượng 1 trong hình chữ nhật
        # từ (0,0) đến (r-1,c-1)
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(n):
                prefix[r + 1][c + 1] = (
                    grid[r][c]
                    + prefix[r][c + 1]
                    + prefix[r + 1][c]
                    - prefix[r][c]
                )

        def get_ones(r: int, c: int, size: int) -> int:
            r2 = r + size
            c2 = c + size

            return (
                prefix[r2][c2]
                - prefix[r][c2]
                - prefix[r2][c]
                + prefix[r][c]
            )

        def dfs(r: int, c: int, size: int) -> 'Node':
            ones = get_ones(r, c, size)

            # toàn 0
            if ones == 0:
                return Node(
                    False,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            # toàn 1
            if ones == size * size:
                return Node(
                    True,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            half = size // 2

            return Node(
                True,      # giá trị bất kỳ vì isLeaf=False
                False,
                dfs(r, c, half),
                dfs(r, c + half, half),
                dfs(r + half, c, half),
                dfs(r + half, c + half, half)
            )

        return dfs(0, 0, n)