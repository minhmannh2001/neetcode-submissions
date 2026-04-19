from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Binary search tìm row
        top = 0
        bottom = m - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][n - 1]:
                top = mid + 1
            else:
                # target nằm trong row này
                row = mid
                break
        else:
            return False

        # Binary search trong row
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False