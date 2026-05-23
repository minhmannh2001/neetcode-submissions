class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        offset = 50000

        count = [0] * 100001

        for num in nums:
            count[num + offset] += 1

        result = []

        for i in range(100001):

            while count[i] > 0:
                result.append(i - offset)
                count[i] -= 1

        return result