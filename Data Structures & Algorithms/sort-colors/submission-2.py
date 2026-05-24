class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0

        # move 0s to front
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        right = len(nums) - 1

        # move 2s to back
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1