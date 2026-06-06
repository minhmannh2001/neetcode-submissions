class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left <= right:

            mid = (left + right) // 2

            current_sum = 0
            subarrays = 1

            for num in nums:

                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = 0

                current_sum += num

            if subarrays <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left