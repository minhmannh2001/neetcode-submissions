class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)
            
            memo[i] = max(rob, skip)
            return memo[i]

        return dfs(0)