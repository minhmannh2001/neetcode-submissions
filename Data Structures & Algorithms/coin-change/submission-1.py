class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        memo = {}

        def dfs(i, remain):
            # base cases
            if remain == 0:
                return 0
            if i == n:
                return float('inf')

            # memo check
            if (i, remain) in memo:
                return memo[(i, remain)]

            res = float('inf')

            # thử dùng coin[i] từ 0 → max
            max_use = remain // coins[i]
            for j in range(max_use + 1):
                next_res = dfs(i + 1, remain - j * coins[i])
                if next_res != float('inf'):
                    res = min(res, next_res + j)

            memo[(i, remain)] = res
            return res

        ans = dfs(0, amount)
        return ans if ans != float('inf') else -1