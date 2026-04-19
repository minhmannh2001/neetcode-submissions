class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1: 
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                    k += 1
                j += 1
            i += 1
        final_res = []
        for triplet in res:
            if sorted(triplet) not in final_res:
                final_res.append(sorted(triplet))
        return final_res