class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for mask in range(1 << n):  # từ 0 → 2^n - 1
            subset = []
            for i in range(n):
                if mask & (1 << i):  # kiểm tra bit thứ i
                    subset.append(nums[i])
            res.append(subset)

        return res