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
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # Đã tìm thấy node cần xóa

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        pred_parent = root
        pred = root.left

        while pred.right:
            pred_parent = pred
            pred = pred.right

        if pred_parent != root:

            pred_parent.right = pred.left

            pred.left = root.left

        pred.right = root.right

        return pred