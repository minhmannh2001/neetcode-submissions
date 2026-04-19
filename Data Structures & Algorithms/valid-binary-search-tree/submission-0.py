class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low, high):
            if not node:
                return True
            
            # check node có nằm trong khoảng hợp lệ không
            if not (low < node.val < high):
                return False
            
            # check left và right
            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )
        
        return dfs(root, float('-inf'), float('inf'))