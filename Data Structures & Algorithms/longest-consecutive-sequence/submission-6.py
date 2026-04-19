class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 not in unique_nums:
                length = 1
                while (num + length) in unique_nums:
                    length += 1
                
                longest = max(longest, length)

        return longest

