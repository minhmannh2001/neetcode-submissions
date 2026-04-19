class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(arr):
            prev2 = 0
            prev1 = 0
            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(
            rob1(nums[:-1]),  # bỏ nhà cuối
            rob1(nums[1:])    # bỏ nhà đầu
        )