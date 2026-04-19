class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute: value -> index trong inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # pre_idx: con trỏ toàn cục trỏ vào root hiện tại trong preorder
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Lấy root, tăng con trỏ
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Tìm vị trí trong inorder O(1)
            mid = inorder_map[root_val]

            # QUAN TRỌNG: build LEFT trước (preorder đi left trước)
            root.left  = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)