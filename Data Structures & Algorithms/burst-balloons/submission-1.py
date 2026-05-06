from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(l: int, r: int) -> int:
            if l + 1 == r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            res = 0
            for k in range(l + 1, r):
                coins = nums[l] * nums[k] * nums[r]
                res = max(
                    res,
                    dfs(l, k) + dfs(k, r) + coins
                )

            memo[(l, r)] = res
            return res

        return dfs(0, len(nums) - 1)