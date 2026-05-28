class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = set()

        for a in range(n):
            for b in range(a + 1, n):
                seen = set()
                for c in range(b + 1, n):
                    need = target - nums[a] - nums[b] - nums[c]
                    if need in seen:
                        quad = tuple(sorted([nums[a], nums[b], nums[c], need]))
                        result.add(quad)
                    seen.add(nums[c])

        return [list(q) for q in result]