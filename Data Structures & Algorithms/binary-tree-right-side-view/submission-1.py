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

                # node đầu tiên (vì đã push right trước)
                if i == 0:
                    res.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res