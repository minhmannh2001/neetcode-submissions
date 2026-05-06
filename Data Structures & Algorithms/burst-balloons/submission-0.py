from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        def dfs(arr: List[int]) -> int:
            if not arr:
                return 0

            key = tuple(arr)
            if key in memo:
                return memo[key]

            n = len(arr)
            res = 0

            for i in range(n):
                left = arr[i - 1] if i - 1 >= 0 else 1
                right = arr[i + 1] if i + 1 < n else 1

                coins = left * arr[i] * right

                # tạo mảng mới sau khi burst i
                new_arr = arr[:i] + arr[i+1:]

                res = max(res, coins + dfs(new_arr))

            memo[key] = res
            return res

        return dfs(nums)