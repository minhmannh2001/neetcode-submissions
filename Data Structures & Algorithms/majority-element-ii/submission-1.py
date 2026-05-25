class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}

        for num in nums:

            count[num] = count.get(num, 0) + 1

        result = []

        limit = len(nums) // 3

        for num, freq in count.items():

            if freq > limit:
                result.append(num)

        return result