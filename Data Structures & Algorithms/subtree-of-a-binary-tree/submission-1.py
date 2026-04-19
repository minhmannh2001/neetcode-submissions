class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):
            if not node:
                return "#"
            
            return f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        root_str = serialize(root)
        sub_str = serialize(subRoot)
        
        return sub_str in root_str