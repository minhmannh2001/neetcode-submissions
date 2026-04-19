class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[num] = idx

            
        