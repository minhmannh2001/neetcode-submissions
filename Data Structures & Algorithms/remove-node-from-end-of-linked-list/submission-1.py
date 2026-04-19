class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast đi trước n bước
        for _ in range(n):
            fast = fast.next

        # cùng đi
        while fast.next:
            fast = fast.next
            slow = slow.next

        # xóa node
        slow.next = slow.next.next

        return dummy.next