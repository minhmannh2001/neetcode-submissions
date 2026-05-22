class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        for i in range(n):

            if nums[i] == val:

                j = i + 1

                while j < n and nums[j] == val:
                    j += 1

                if j < n:
                    nums[i], nums[j] = nums[j], nums[i]

        k = 0

        for num in nums:
            if num != val:
                k += 1

        return k