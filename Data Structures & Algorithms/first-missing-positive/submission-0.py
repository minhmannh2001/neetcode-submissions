class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        target = 1

        while True:

            found = False

            for num in nums:

                if num == target:
                    found = True
                    break

            if not found:
                return target

            target += 1