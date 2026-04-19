class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for idx2 in range(idx1 + 1, len(nums)):
                if num1 + nums[idx2] == target:
                    return [idx1, idx2]
        return []

            
        