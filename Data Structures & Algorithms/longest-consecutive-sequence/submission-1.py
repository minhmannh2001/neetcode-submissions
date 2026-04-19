class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest_consecutive = 0
        longest_consecutive_to_current = [1] * len(sorted_nums)
        for i, num in enumerate(sorted_nums):
            if i == 0:
                continue
            else:
                if num - sorted_nums[i - 1] == 1:
                    longest_consecutive_to_current[i] = longest_consecutive_to_current[i - 1] + 1
                elif num == sorted_nums[i - 1]:
                    longest_consecutive_to_current[i] = longest_consecutive_to_current[i - 1]
        for v in longest_consecutive_to_current:
            if v > longest_consecutive:
                longest_consecutive = v
        return longest_consecutive

        