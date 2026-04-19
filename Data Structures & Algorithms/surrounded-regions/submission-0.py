from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        # Bước 1: Đẩy tất cả 'O' trên biên vào Queue và đánh dấu chúng
        queue = deque()
        
        # Duyệt 4 cạnh biên
        for i in range(rows):
            # Cạnh trái
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'T'   # T = Temporary (đánh dấu không bị bao quanh)
            # Cạnh phải
            if board[i][cols-1] == 'O':
                queue.append((i, cols-1))
                board[i][cols-1] = 'T'
        
        for j in range(cols):
            # Cạnh trên
            if board[0][j] == 'O':
                queue.append((0, j))
                board[0][j] = 'T'
            # Cạnh dưới
            if board[rows-1][j] == 'O':
                queue.append((rows-1, j))
                board[rows-1][j] = 'T'
        
        # Bước 2: BFS từ các ô biên, lan ra đánh dấu tất cả 'O' nối liền
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                    board[nx][ny] = 'T'
                    queue.append((nx, ny))
        
        # Bước 3: Duyệt toàn board để quyết định cuối cùng
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'      # Bị bao quanh → đổi thành X
                elif board[i][j] == 'T':
                    board[i][j] = 'O'      # Không bị bao quanh → giữ O