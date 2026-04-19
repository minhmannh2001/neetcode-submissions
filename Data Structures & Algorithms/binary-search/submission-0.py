class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        else:
            mid = len(nums) // 2
            result1 = self.search(nums[:mid], target)
            result2 = self.search(nums[mid:], target)
            if result1 != -1:
                return 0 + result1
            elif result2 != -1:
                return mid + result2
            else:
                return -1
        