class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head

        while current and current.next:
            # tìm node cuối và node trước nó
            prev = None
            tail = current

            while tail.next:
                prev = tail
                tail = tail.next

            # nếu tail trùng current hoặc next thì dừng
            if tail == current or tail == current.next:
                break

            # cắt tail ra
            prev.next = None

            # chèn tail vào sau current
            tail.next = current.next
            current.next = tail

            # move current
            current = tail.next