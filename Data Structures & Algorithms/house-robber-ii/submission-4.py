class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            rob = arr[i] + dfs(i+2, arr, memo)
            skip = dfs(i+1, arr, memo)
            
            memo[i] = max(rob, skip)
            return memo[i]

        if len(nums) == 1:
            return nums[0]

        # case 1: bỏ nhà cuối
        memo1 = [-1] * (len(nums) - 1)
        res1 = dfs(0, nums[:-1], memo1)

        # case 2: bỏ nhà đầu
        memo2 = [-1] * (len(nums) - 1)
        res2 = dfs(0, nums[1:], memo2)

        return max(res1, res2)