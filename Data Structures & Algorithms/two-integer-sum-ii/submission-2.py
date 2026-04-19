class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        
        for i in range(n):
            for j in range(i + 1, n):
                current_sum = numbers[i] + numbers[j]
                
                if current_sum == target:
                    return [i + 1, j + 1]
                
                if current_sum > target:
                    break
