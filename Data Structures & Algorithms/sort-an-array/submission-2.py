import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quick_sort(left, right):

            if left >= right:
                return

            pivot_index = random.randint(left, right)

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            pivot = nums[right]

            p = left

            for i in range(left, right):

                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            quick_sort(left, p - 1)
            quick_sort(p + 1, right)

        quick_sort(0, len(nums) - 1)

        return nums