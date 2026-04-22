class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        
        prefix = 1
        suffix = 1
        
        n = len(nums)
        
        for i in range(n):
            # từ trái sang
            prefix *= nums[i]
            
            # từ phải sang
            suffix *= nums[n - 1 - i]
            
            res = max(res, prefix, suffix)
            
            # reset khi gặp 0
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        
        return res