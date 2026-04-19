class Solution:
    def reverseKGroup(self, head, k):
        # 1. check đủ k node
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        # 2. reverse k node đầu
        prev = None
        curr = head

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. nối với phần còn lại (recursion)
        head.next = self.reverseKGroup(curr, k)

        return prev