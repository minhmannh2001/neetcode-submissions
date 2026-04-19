class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                remain = -(nums[i] + nums[j])
                if count[remain] > 0:
                    res.append([nums[i], nums[j], remain])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res
