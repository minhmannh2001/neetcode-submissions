class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for s in range(target + 1):
                dp[i][s] = dp[i-1][s]
                
                if s >= nums[i-1]:
                    dp[i][s] |= dp[i-1][s - nums[i-1]]
        
        return dp[n][target]