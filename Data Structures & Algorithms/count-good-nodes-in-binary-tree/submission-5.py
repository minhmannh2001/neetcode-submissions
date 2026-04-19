from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])
        count = 0
        
        while queue:
            node, current_max = queue.popleft()
            
            if node.val >= current_max:
                count += 1
            
            new_max = max(current_max, node.val)
            
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
        
        return count