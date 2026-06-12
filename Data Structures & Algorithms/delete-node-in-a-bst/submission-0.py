class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1 + Case 2

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Case 3: có cả left và right

            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(
                root.right,
                successor.val
            )

        return root