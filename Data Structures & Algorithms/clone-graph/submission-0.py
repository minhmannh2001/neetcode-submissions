from collections import deque

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        # map: original -> clone
        clone_map = {}

        queue = deque([node])
        clone_map[node] = Node(node.val)

        while queue:
            cur = queue.popleft()

            for nei in cur.neighbors:
                # nếu chưa clone
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val)
                    queue.append(nei)

                # nối neighbor
                clone_map[cur].neighbors.append(clone_map[nei])

        return clone_map[node]