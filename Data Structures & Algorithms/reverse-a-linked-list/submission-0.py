class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # lưu node tiếp theo
            curr.next = prev        # đảo chiều
            prev = curr             # cập nhật prev
            curr = next_node        # di chuyển

        return prev