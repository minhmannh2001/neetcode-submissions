class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            stack = []
            curr = prev.next

            # push k node
            for _ in range(k):
                if not curr:
                    return dummy.next
                stack.append(curr)
                curr = curr.next

            # pop để reverse
            while stack:
                prev.next = stack.pop()
                prev = prev.next

            prev.next = curr