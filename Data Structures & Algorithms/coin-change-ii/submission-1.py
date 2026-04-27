from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(remaining, start):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            combinations = 0
            for i in range(start, len(coins)):
                combinations += dfs(remaining - coins[i], i)
            
            return combinations
        
        return dfs(amount, 0)