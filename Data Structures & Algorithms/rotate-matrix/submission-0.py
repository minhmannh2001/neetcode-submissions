from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        # Create copy
        temp = [row[:] for row in matrix]
        
        # Put values into rotated positions
        for row in range(n):
            for col in range(n):
                
                matrix[col][n - 1 - row] = temp[row][col]