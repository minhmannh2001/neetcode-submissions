class Solution:
    def insertIntoBST(self, root, val):

        if root is None:
            return TreeNode(val)

        curr = root

        while True:

            if val < curr.val:

                if curr.left is None:
                    curr.left = TreeNode(val)
                    break

                curr = curr.left

            else:

                if curr.right is None:
                    curr.right = TreeNode(val)
                    break

                curr = curr.right

        return root