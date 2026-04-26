from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i: int, canBuy: bool) -> int:
            # base case
            if i >= n:
                return 0

            if canBuy:
                # option 1: buy
                buy = -prices[i] + dfs(i + 1, False)
                # option 2: skip
                skip = dfs(i + 1, True)
                return max(buy, skip)
            else:
                # option 1: sell (cooldown → i+2)
                sell = prices[i] + dfs(i + 2, True)
                # option 2: hold
                hold = dfs(i + 1, False)
                return max(sell, hold)

        return dfs(0, True)