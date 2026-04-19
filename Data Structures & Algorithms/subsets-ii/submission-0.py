class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(start, path):
            res.add(tuple(sorted(path)))  # ❗ sort để tránh khác thứ tự

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return [list(x) for x in res]