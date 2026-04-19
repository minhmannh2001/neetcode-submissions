class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def max_gain(node):
            """Trả về gain lớn nhất từ node này đi XUỐNG 1 nhánh"""
            if not node:
                return 0
            left  = max(max_gain(node.left),  0)  # bỏ nếu âm
            right = max(max_gain(node.right), 0)  # bỏ nếu âm
            return node.val + max(left, right)
        
        def all_nodes(node):
            """Lấy tất cả nodes trong cây"""
            if not node:
                return []
            return [node] + all_nodes(node.left) + all_nodes(node.right)
        
        # Với MỖI node làm đỉnh, tính path sum qua node đó
        res = float('-inf')
        for node in all_nodes(root):
            left  = max(max_gain(node.left),  0)
            right = max(max_gain(node.right), 0)
            # path đi qua node này làm đỉnh
            path_sum = node.val + left + right
            res = max(res, path_sum)
        
        return res