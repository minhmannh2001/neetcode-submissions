class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(i, xor):
            nonlocal ans

            if i == len(nums):
                ans += xor
                return

            dfs(i + 1, xor)
            dfs(i + 1, xor ^ nums[i])

        dfs(0, 0)
        return ans