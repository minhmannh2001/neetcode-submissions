class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count > 0:
                if num == 0:
                    res[i] = prod
            elif zero_count == 0:
                res[i] = prod // num

        return res
        
            

        