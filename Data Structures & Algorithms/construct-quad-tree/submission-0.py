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

        def dfs(size: int, r: int, c: int) -> 'Node':
            first = grid[r][c]

            is_leaf = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        is_leaf = False
                        break

                if not is_leaf:
                    break

            if is_leaf:
                return Node(
                    first == 1,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            half = size // 2

            topLeft = dfs(half, r, c)
            topRight = dfs(half, r, c + half)
            bottomLeft = dfs(half, r + half, c)
            bottomRight = dfs(half, r + half, c + half)

            return Node(
                True,      # val có thể là True hoặc False khi isLeaf=False
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return dfs(len(grid), 0, 0)