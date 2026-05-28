class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for a in range(n):

            # skip duplicate a
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n):

                # skip duplicate b
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                lo, hi = b + 1, n - 1

                while lo < hi:
                    s = nums[a] + nums[b] + nums[lo] + nums[hi]

                    if s == target:
                        result.append([
                            nums[a],
                            nums[b],
                            nums[lo],
                            nums[hi]
                        ])

                        lo += 1
                        hi -= 1

                        # skip duplicate lo
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1

                        # skip duplicate hi
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

                    elif s < target:
                        lo += 1

                    else:
                        hi -= 1

        return result