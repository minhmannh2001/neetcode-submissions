from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # node cuối cùng của level
                if i == level_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res