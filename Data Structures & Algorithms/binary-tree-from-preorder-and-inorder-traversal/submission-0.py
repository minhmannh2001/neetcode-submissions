class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Bước 1: root luôn là phần tử đầu preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Bước 2: tìm vị trí root trong inorder — O(n) mỗi lần gọi
        mid = inorder.index(root_val)

        # Bước 3: chia đôi và đệ quy
        # left subtree có `mid` phần tử
        root.left  = self.buildTree(preorder[1 : mid + 1],
                                    inorder[:mid])

        root.right = self.buildTree(preorder[mid + 1:],
                                    inorder[mid + 1:])

        return root