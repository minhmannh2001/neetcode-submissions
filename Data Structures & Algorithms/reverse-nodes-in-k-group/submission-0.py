class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # 1. kiểm tra có đủ k node không
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # không đủ k → dừng

            group_next = kth.next

            # 2. reverse group
            prev = group_next
            curr = group_prev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. nối lại list
            temp = group_prev.next  # sẽ là tail sau khi reverse
            group_prev.next = prev
            group_prev = temp