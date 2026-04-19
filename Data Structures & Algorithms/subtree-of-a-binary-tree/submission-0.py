class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        if not root:
            return False
        
        # nếu match ngay tại node này
        if isSame(root, subRoot):
            return True
        
        # thử tiếp bên trái và phải
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)