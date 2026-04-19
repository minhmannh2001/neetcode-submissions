import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def dfs(node):
            if not node:
                return
            
            heapq.heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)