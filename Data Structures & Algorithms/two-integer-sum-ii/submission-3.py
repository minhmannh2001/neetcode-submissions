import bisect

class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        
        for i in range(n):
            remain = target - numbers[i]
            
            # tìm trong phần còn lại
            index = bisect.bisect_left(numbers, remain, i + 1)
            
            if index < n and numbers[index] == remain:
                return [i + 1, index + 1]
