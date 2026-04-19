class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clone_map = {}

        def dfs(cur):
            if cur in clone_map:
                return clone_map[cur]

            copy = Node(cur.val)
            clone_map[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)