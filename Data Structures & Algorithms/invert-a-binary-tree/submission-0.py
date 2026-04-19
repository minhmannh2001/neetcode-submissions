class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # đảo trái phải
        root.left, root.right = root.right, root.left
        
        # đệ quy xuống dưới
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root