from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        # Step 1: transpose
        for row in range(n):
            for col in range(row + 1, n):
                
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )
        
        # Step 2: reverse each row
        for row in matrix:
            row.reverse()