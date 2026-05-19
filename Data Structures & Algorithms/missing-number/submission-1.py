from typing import List


class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        
        seen = set(nums)
        
        n = len(nums)
        
        for x in range(n + 1):
            
            if x not in seen:
                return x