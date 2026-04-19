class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        def dfs(node):
            if not node:
                return 0
            
            count = dfs(node.next) + 1

            # nếu node.next là node cần xóa
            if count == n + 1:
                node.next = node.next.next
            
            return count

        dfs(dummy)
        return dummy.next