class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        curr = root

        while curr:

            if curr.left is None:

                result.append(curr.val)

                curr = curr.right

            else:

                predecessor = curr.left

                while (
                    predecessor.right is not None
                    and predecessor.right != curr
                ):
                    predecessor = predecessor.right

                if predecessor.right is None:

                    result.append(curr.val)

                    predecessor.right = curr

                    curr = curr.left

                else:

                    predecessor.right = None

                    curr = curr.right

        return result