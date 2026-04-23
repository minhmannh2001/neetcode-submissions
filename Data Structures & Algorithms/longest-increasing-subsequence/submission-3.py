from functools import lru_cache
import sys

sys.setrecursionlimit(2000)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, prev_i):
            if i == len(nums):
                return 0
            
            # skip
            res = dfs(i + 1, prev_i)
            
            # take
            if prev_i == -1 or nums[i] > nums[prev_i]:
                res = max(res, 1 + dfs(i + 1, i))
            
            return res
        
        return dfs(0, -1)