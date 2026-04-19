class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        
        if not root:
            return 0
        
        # đường kính đi qua root
        diameter = depth(root.left) + depth(root.right)
        
        # đường kính nằm hoàn toàn bên trái hoặc phải
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(diameter, left_diameter, right_diameter)