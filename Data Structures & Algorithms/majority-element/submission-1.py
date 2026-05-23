class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for num in nums:
            count = 0

            for x in nums:
                if x == num:
                    count += 1

            if count > n // 2:
                return num