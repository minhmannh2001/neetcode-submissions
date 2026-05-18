from typing import List


class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            
            found_duplicate = False
            
            for j in range(len(nums)):
                
                if i != j and nums[i] == nums[j]:
                    found_duplicate = True
                    break
            
            if not found_duplicate:
                return nums[i]