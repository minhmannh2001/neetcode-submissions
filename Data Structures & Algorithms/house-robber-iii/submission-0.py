# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}

        def dfs(node: Optional[TreeNode], can_rob: bool) -> int:
            if not node:
                return 0

            key = (node, can_rob)

            if key in memo:
                return memo[key]

            # Không được phép rob node hiện tại
            if not can_rob:
                result = (
                    dfs(node.left, True)
                    + dfs(node.right, True)
                )
            else:
                # Option 1: Rob node hiện tại
                take = (
                    node.val
                    + dfs(node.left, False)
                    + dfs(node.right, False)
                )

                # Option 2: Không rob node hiện tại
                skip = (
                    dfs(node.left, True)
                    + dfs(node.right, True)
                )

                result = max(take, skip)

            memo[key] = result
            return result

        return dfs(root, True)