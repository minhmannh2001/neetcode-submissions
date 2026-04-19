class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        # Output: "1,2,N,N,3,N,N"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        self.i = 0          # con trỏ toàn cục, giống bài build tree

        def dfs():
            if tokens[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(tokens[self.i]))
            self.i += 1
            node.left  = dfs()
            node.right = dfs()
            return node

        return dfs()