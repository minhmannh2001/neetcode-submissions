class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        # lọc bỏ list rỗng ban đầu
        lists = [node for node in lists if node]

        while lists:
            min_index = 0

            # tìm node nhỏ nhất trong các head
            for i in range(len(lists)):
                if lists[i].val < lists[min_index].val:
                    min_index = i

            # lấy node nhỏ nhất
            min_node = lists[min_index]

            # add vào result
            current.next = min_node
            current = current.next

            # move pointer của list đó
            lists[min_index] = min_node.next

            # nếu list đó hết → remove khỏi lists
            if lists[min_index] is None:
                lists.pop(min_index)

        return dummy.next