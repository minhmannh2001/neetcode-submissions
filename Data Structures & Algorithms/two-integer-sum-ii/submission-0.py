from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        # Duyệt tất cả cặp (i, j)
        for i in range(n):
            for j in range(n):
                # Không được dùng cùng 1 phần tử
                if i != j:
                    if numbers[i] + numbers[j] == target:
                        # Trả về 1-indexed
                        return [i + 1, j + 1]
