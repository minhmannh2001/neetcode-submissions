class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = []
        for i, num in enumerate(nums):
            if len(left_products) == 0:
                left_products.append(num)
            else:
                left_products.append(left_products[i - 1] * num)

        right_products = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_products.insert(0, nums[i])
            else:
                right_products.insert(0, right_products[0] * nums[i])

        res = []
        for i, num in enumerate(nums):
            if i == 0:
                res.append(right_products[i + 1])
            elif i == len(nums) - 1:
                res.append(left_products[i - 1])
            else:
                res.append(left_products[i - 1] * right_products[i + 1])

        return res
        
            

        