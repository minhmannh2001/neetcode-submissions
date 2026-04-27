class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(remaining_nums, current):
            if current == target and len(remaining_nums) == 0:
                return 1
            
            if len(remaining_nums) == 0:
                return 0

            return dfs(remaining_nums[1:], current + remaining_nums[0]) + dfs(remaining_nums[1:], current - remaining_nums[0])
            
        return dfs(nums, 0)
        