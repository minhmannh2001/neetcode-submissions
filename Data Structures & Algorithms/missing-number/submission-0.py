from typing import List


class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for x in range(n + 1):
            
            if x not in nums:
                return x