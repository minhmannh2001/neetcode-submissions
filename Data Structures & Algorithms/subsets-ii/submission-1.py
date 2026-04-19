class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 🔑 quan trọng

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                # 🔥 skip duplicate
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res