class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        
        def dfs(node):
            if not node:
                return "#"
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            cur = f"{node.val},{left},{right}"
            
            if cur == sub_hash:
                self.found = True
            
            return cur
        
        def build_hash(node):
            if not node:
                return "#"
            return f"{node.val},{build_hash(node.left)},{build_hash(node.right)}"
        
        sub_hash = build_hash(subRoot)
        dfs(root)
        
        return self.found