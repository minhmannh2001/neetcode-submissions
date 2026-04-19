class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Gain từ nhánh trái/phải, bỏ nếu âm
            left  = max(dfs(node.left),  0)
            right = max(dfs(node.right), 0)

            # Tại node này làm ĐỈNH: cộng cả 2 nhánh → update global
            self.res = max(self.res, node.val + left + right)

            # Trả lên cha: chỉ được chọn 1 nhánh
            return node.val + max(left, right)

        dfs(root)
        return self.res