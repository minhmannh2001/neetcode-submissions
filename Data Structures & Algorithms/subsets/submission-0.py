class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, path, k):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path, k)
                path.pop()

        for k in range(n + 1):
            backtrack(0, [], k)

        return res