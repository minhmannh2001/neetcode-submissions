class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        stack = []
        
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        # pop n node
        for _ in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next

        return dummy.next