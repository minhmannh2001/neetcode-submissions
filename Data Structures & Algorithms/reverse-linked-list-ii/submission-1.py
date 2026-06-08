class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # prev_left = node đứng trước vị trí left
        prev_left = dummy
        for _ in range(left - 1):
            prev_left = prev_left.next

        # left_node sẽ trở thành đuôi sau khi reverse
        left_node = prev_left.next

        prev = None
        curr = left_node

        # reverse (right - left + 1) nodes
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # nối lại
        prev_left.next = prev
        left_node.next = curr

        return dummy.next