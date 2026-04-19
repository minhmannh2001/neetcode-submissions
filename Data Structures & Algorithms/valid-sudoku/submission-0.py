from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1️⃣ Check từng hàng
        for row in range(9):
            for col1 in range(9):
                if board[row][col1] == ".":
                    continue
                
                for col2 in range(col1 + 1, 9):
                    if board[row][col1] == board[row][col2]:
                        return False
        
        # 2️⃣ Check từng cột
        for col in range(9):
            for row1 in range(9):
                if board[row1][col] == ".":
                    continue
                
                for row2 in range(row1 + 1, 9):
                    if board[row1][col] == board[row2][col]:
                        return False
        
        # 3️⃣ Check từng box 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                
                for i in range(3):
                    for j in range(3):
                        if board[box_row + i][box_col + j] == ".":
                            continue
                        
                        for x in range(i, 3):
                            for y in range(3):
                                if x == i and y <= j:
                                    continue
                                
                                if board[box_row + i][box_col + j] == board[box_row + x][box_col + y]:
                                    return False
        
        return True
