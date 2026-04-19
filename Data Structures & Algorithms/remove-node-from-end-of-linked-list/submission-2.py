class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        # đếm length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # đi tới node trước node cần xóa
        cur = dummy
        for _ in range(length - n):
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next