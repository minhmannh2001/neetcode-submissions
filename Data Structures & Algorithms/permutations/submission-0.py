class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []

        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]  # ❌ tạo list mới
            perms = self.permute(rest)

            for p in perms:
                res.append([nums[i]] + p)

        return res