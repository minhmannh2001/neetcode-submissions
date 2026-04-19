class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, idx):
            # điều kiện dừng: tìm được hết word
            if idx == len(word):
                return True

            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # ô đã dùng rồi
            if (r, c) in visited:
                return False

            # ký tự không khớp
            if board[r][c] != word[idx]:
                return False

            # đánh dấu đang dùng ô này
            visited.add((r, c))

            # tìm 4 ô xung quanh với ký tự tiếp theo
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))

            # bỏ đánh dấu để các path khác dùng lại được
            visited.remove((r, c))

            return found

        # loop qua tất cả ký tự, tìm ký tự đầu tiên của word
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:   # ký tự đầu khớp
                    if dfs(r, c, 0):
                        return True

        return False