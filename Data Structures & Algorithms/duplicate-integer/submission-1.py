class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_values = {}
        for num in nums:
            if distinct_values.get(num) == 1:
                return True
            distinct_values[num] = 1
        return False