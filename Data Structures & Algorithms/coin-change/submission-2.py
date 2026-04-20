from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        INF = float('inf')

        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return INF
            if remain in memo:
                return memo[remain]

            res = INF
            for coin in coins:
                res = min(res, 1 + dfs(remain - coin))

            memo[remain] = res
            return res

        ans = dfs(amount)
        return ans if ans != INF else -1