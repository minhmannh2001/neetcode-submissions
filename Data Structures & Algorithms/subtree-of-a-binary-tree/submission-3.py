class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        
        def dfs(node):
            if not node:
                return 3  # base hash
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # tạo hash (Merkle style)
            cur = hash((node.val, left, right))
            
            if cur == sub_hash:
                self.found = True
            
            return cur
        
        def get_hash(node):
            if not node:
                return 3
            return hash((node.val, get_hash(node.left), get_hash(node.right)))
        
        sub_hash = get_hash(subRoot)
        dfs(root)
        
        return self.found