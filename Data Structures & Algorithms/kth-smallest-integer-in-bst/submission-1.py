class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node:
                return None
            
            left = inorder(node.left)
            if left is not None:
                return left
            
            k -= 1
            if k == 0:
                return node.val
            
            return inorder(node.right)
        
        return inorder(root)