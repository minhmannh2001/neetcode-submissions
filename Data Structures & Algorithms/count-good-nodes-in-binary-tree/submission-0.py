class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node: TreeNode, current_max: int):
            if not node:
                return
            
            # nếu node hiện tại >= max trên path → good node
            if node.val >= current_max:
                self.count += 1
            
            # update max cho path tiếp theo
            new_max = max(current_max, node.val)
            
            # duyệt tiếp left và right
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        # bắt đầu từ root
        dfs(root, root.val)
        
        return self.count