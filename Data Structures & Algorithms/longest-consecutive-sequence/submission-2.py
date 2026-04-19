class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        res = 0
        for num in nums:
            streak, cur = 0, num
            while cur in unique_nums:
                streak += 1
                cur += 1
            if streak > res:
                res = streak
        
        return res