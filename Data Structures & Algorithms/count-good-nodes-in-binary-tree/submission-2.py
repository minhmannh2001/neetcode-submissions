class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if not node:
                return 0
            
            good = 1 if node.val >= current_max else 0
            new_max = max(current_max, node.val)
            
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)
        
        return dfs(root, root.val)