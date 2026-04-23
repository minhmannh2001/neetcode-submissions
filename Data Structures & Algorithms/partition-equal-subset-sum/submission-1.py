from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        @lru_cache(None)
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i == len(nums) or curr_sum > target:
                return False
            
            return (
                dfs(i + 1, curr_sum + nums[i]) or
                dfs(i + 1, curr_sum)
            )
        
        return dfs(0, 0)