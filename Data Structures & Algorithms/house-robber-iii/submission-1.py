class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if not node:
                return (0, 0)

            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            rob_this = (
                node.val
                + left_not
                + right_not
            )

            skip_this = (
                max(left_rob, left_not)
                + max(right_rob, right_not)
            )

            return (rob_this, skip_this)

        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)