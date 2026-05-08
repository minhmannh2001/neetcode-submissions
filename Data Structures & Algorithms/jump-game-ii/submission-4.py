import sys
sys.setrecursionlimit(10**6)

class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            # đã tới hoặc vượt cuối mảng
            if i >= len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]

            min_steps = float("inf")

            # thử mọi bước nhảy có thể
            for jump in range(nums[i], 0, -1):
                steps = 1 + dfs(i + jump)
                min_steps = min(min_steps, steps)

            memo[i] = min_steps
            return min_steps

        return dfs(0)