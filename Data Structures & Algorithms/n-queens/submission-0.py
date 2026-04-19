class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def can_attack(queens: List[tuple], row: int, col: int) -> bool:
            """check xem ô (row,col) có bị queen nào tấn công không"""
            for qr, qc in queens:
                # cùng cột
                if qc == col:
                    return True
                # cùng đường chéo
                # 2 điểm cùng đường chéo khi |row1-row2| == |col1-col2|
                if abs(qr - row) == abs(qc - col):
                    return True
            return False

        result = []

        def backtrack(row: int, queens: List[tuple]):
            # điều kiện dừng: đã đặt đủ n queens
            if row == n:
                # convert queens positions → board
                board = []
                for _, qc in queens:
                    board.append('.' * qc + 'Q' + '.' * (n - qc - 1))
                result.append(board)
                return

            # thử đặt queen ở từng cột của hàng hiện tại
            for col in range(n):
                if not can_attack(queens, row, col):
                    queens.append((row, col))       # đặt queen
                    backtrack(row + 1, queens)      # xuống hàng tiếp
                    queens.pop()                    # backtrack

        backtrack(0, [])
        return result