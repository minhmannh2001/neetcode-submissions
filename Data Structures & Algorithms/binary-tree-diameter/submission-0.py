class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # cập nhật diameter
            self.max_diameter = max(self.max_diameter, left + right)
            
            # trả về depth
            return max(left, right) + 1
        
        dfs(root)
        return self.max_diameter