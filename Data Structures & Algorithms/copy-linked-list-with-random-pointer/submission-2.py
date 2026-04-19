class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_nodes = []
        curr = head
        
        # lưu node cũ
        while curr:
            old_nodes.append(curr)
            curr = curr.next

        # tạo node mới
        new_nodes = [Node(node.val) for node in old_nodes]

        # nối next + random
        for i in range(len(old_nodes)):
            if i + 1 < len(old_nodes):
                new_nodes[i].next = new_nodes[i + 1]

            if old_nodes[i].random:
                # tìm index của random
                j = old_nodes.index(old_nodes[i].random)
                new_nodes[i].random = new_nodes[j]

        return new_nodes[0]