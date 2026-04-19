class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # 🔑 sort trước

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                # 🔥 pruning quan trọng
                if total + nums[i] > target:
                    break  # vì đã sort nên phía sau còn lớn hơn nữa

                path.append(nums[i])
                backtrack(i, path, total + nums[i])  # reuse
                path.pop()

        backtrack(0, [], 0)
        return res