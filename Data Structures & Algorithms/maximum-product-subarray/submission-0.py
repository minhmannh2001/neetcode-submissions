class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # vì cur_max sẽ bị update nên phải lưu tạm
            temp_max = max(num, num * cur_max, num * cur_min)
            temp_min = min(num, num * cur_max, num * cur_min)

            cur_max = temp_max
            cur_min = temp_min

            result = max(result, cur_max)

        return result