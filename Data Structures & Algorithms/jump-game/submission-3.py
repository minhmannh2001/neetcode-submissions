class Solution:
    def canJump(self, nums):
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if i in memo:
                return memo[i]

            # Try larger jumps first to reach the end faster and reduce recursion depth
            for jump in range(nums[i], 0, -1):
                if dfs(i + jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)