class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i == len(nums) or curr_sum > target:
                return False
            
            # take
            if dfs(i + 1, curr_sum + nums[i]):
                return True
            
            # skip
            return dfs(i + 1, curr_sum)
        
        return dfs(0, 0)